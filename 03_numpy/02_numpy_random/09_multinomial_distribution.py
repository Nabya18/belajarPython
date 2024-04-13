"""
Distribusi Multinomial
1. Distribusi multinomial merupakan generalisasi dari distribusi binomial.
2. Ini menggambarkan hasil dari skenario multi-nomial, tidak seperti binomial yang skenarionya harus hanya satu dari dua. misalnya golongan darah suatu populasi, hasil pelemparan dadu.
3. Ini memiliki tiga parameter:
    n-      jumlah hasil yang mungkin (misalnya 6 untuk pelemparan dadu).
    pvals-  daftar probabilitas hasil (misalnya [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] untuk pelemparan dadu).
    size-   Bentuk array yang dikembalikan.
"""
# Gambarlah contoh pelemparan dadu
from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

"""
Catatan: Sampel multinomial TIDAK akan menghasilkan nilai tunggal! Mereka akan menghasilkan satu nilai untuk masing-masingnya pval.
Catatan: Karena merupakan generalisasi dari distribusi binomial, representasi visual dan kesamaan distribusi normalnya sama dengan distribusi binomial berganda.


Kode ini menghasilkan sampel acak dari distribusi multinomial dengan parameter n=6 dan pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]. 
Distribusi multinomial adalah generalisasi dari distribusi binomial yang digunakan ketika masing-masing dari beberapa kategori memiliki kemungkinan keberhasilan yang berbeda.

Parameter n menentukan jumlah percobaan yang akan dilakukan, dalam hal ini, jumlahnya adalah 6.

Parameter pvals adalah sebuah array yang berisi probabilitas keberhasilan untuk setiap kategori. Dalam kasus ini, setiap kategori memiliki probabilitas yang sama, yaitu 1/6.

Hasilnya adalah sebuah array yang berisi jumlah kejadian yang terjadi untuk setiap kategori dalam percobaan tersebut.
"""