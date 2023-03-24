# Word Segmentation
Word Segmentation merupakan sebuah alat untuk melakukan proses preprocessing pada teks untuk memperbaiki teks yang bersambung sehingga berdiri sendiri dan juga untuk memperbaiki kesalahan ketik pada teks (typo). Word Segmentation ini menggunakan corpus dari wikipedia Indonesia.

Word segmentation mengacu pada [ekpharasis](https://github.com/cbaziotis/ekphrasis)

# Cara Menggunakan
1. clone repository ini
 ```
git clone https://github.com/Alfaalputra/word_segmentation.git
 ```
2. Install requirements.txt
```
pip install -r requirements.txt
```
3. Buat folder bernama data
4. Jalankan get_wiki.py untuk mendownload idwikipedia
```
python get_wiki.py
```
5. Jalankan get_data.py untuk mengekstrak data wikipedia
```
python get_data.py
```
6. Jalankan generate_stats.py untuk membuat corpus sebanyak N-grams
```
python generate_stats.py --input wiki_corpus.txt --name wiki_corpus --ngrams 2 --mincount 1 1
```

# Word Segmentation
Contoh penggunaan word segmentation berikut:
```python
from src.segmentation import Segmentation
seg = Segmentation(corpus="wiki_corpus") 
print(seg.segment("sayainginmakan"))
```
Output:
```
saya ingin makan
```
# Word Correction
Contoh penggunaan word correction berikut:
```python
from src.correction import Correction
cor = Correction(corpus="wiki_corpus")
print(cor.correct("kwenapah"))
```
Output:
```
kenapa
```