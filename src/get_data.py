import io
import time
import gensim
from datetime import timedelta


if __name__ == '__main__':
    
    start_time = time.time()    
    print('Streaming wiki...')
    id_wiki = gensim.corpora.WikiCorpus(
        'data/idwiki-latest-pages-articles.xml.bz2',
        dictionary={}, lower=False
    )
    
    article_count = 0
    with io.open('data/wiki_corpus.txt', 'w', encoding='utf-8') as wiki_txt:
        for text in id_wiki.get_texts():

            wiki_txt.write(" ".join(text) + '\n')
            article_count += 1

            if article_count % 10000 == 0:
                print('{} articles processed'.format(article_count))
        print('total: {} articles'.format(article_count))

    finish_time = time.time()
    print('Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))