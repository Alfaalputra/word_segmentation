import requests
from clint.textui import progress

if __name__ == '__main__':
    url = 'https://dumps.wikimedia.org/idwiki/latest/idwiki-latest-pages-articles.xml.bz2'
    r = requests.get(url, stream=True)
    path = 'data/idwiki-latest-pages-articles.xml.bz2'
    print("Downloading dataset from idwiki latest pages articles")
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()
    print("Download complete")