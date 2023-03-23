from functools import reduce
import operator
import os
from os import path
import sys
import inspect
import ujson as json
from urllib.request import urlretrieve
import zipfile

path_this = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(path_this, '..'))
sys.path.append(root_dir)
class Helpers:

    def get_stats_dir(self):
        
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)

        stats_dir = path.join(root_dir, 'stats')

        if not os.path.exists(stats_dir):
            os.makedirs(stats_dir)

        return stats_dir


    def parse_stats(self, name, sep='\t', ngram_sep='_'):
        """
        Read key,value pairs from file.
        """
        print("reading ngrams", name)
        d = {}
        with open(name, "r", encoding="utf-8") as f:
            for line in f:
                values = line.split(sep)
                if len(values) > 2:
                    d[ngram_sep.join(values[:-1])] = int(values[-1])
                else:
                    d[values[0]] = int(values[1])

        return d


    def read_stats(self, corpus, ngram):
        stats_dir = self.get_stats_dir()
        self.check_stats_files()
        print("Reading " + "{} - {}grams ...".format(corpus, ngram))
        text = path.join(*[stats_dir, corpus, "counts_{}grams.txt".format(ngram)])
        dumped = path.join(
            *[stats_dir, corpus, "counts_{}grams.json".format(ngram)])

        if os.path.isfile(dumped):
            with open(dumped, "r") as f:
                stats = json.load(f)
                return stats
        elif os.path.isfile(text):
            print("generating cache file for faster loading...")
            stats = self.parse_stats(text)
            with open(dumped, "w") as f:
                json.dump(stats, f)
            return stats
        else:
            print("stats file not available!")
            sys.exit(1)


    def listdir_nohidden(self, path):
        return [f for f in os.listdir(path) if not f.startswith('.')]


    def download_statistics(self):
        stats_dir = self.get_stats_dir()
        print("Word statistics files not found!\nDownloading...", end=" ")
        url = "https://data.statmt.org/cbaziotis/projects/ekphrasis/stats.zip"
        urlretrieve(url, "stats.zip")
        print("done!")

        print("Unpacking...", end=" ")
        with zipfile.ZipFile("stats.zip", "r") as zip_ref:
            zip_ref.extractall(stats_dir)

        os.remove("stats.zip")
        print("done!")


    def check_stats_files(self):
        stats_dir = self.get_stats_dir()
        if not os.path.exists(stats_dir) or len(self.listdir_nohidden(stats_dir)) == 0:
            self.download_statistics()


    def product(self, nums):
        """
        Return the product of a sequence of numbers.
        """
        return reduce(operator.mul, nums, 1)

    def remove_tags(doc):
        """
        Remove tags from sentence
        """
        doc = ' '.join(word for word in doc.split() if word[0]!='<')
        return doc