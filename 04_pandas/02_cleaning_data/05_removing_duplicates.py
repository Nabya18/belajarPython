"""
Pandas - Menghapus Duplikat

Menemukan Duplikat => Baris duplikat adalah baris yang telah didaftarkan lebih dari satu kali.
    1. Untuk menemukan duplikat, kita bisa menggunakan duplicated()metode tersebut.
    2. Metode ini duplicated() mengembalikan nilai Boolean untuk setiap baris

Catatan: (inplace = True) akan memastikan bahwa metode ini TIDAK mengembalikan DataFrame baru , tetapi akan menghapus semua duplikat dari DataFrame asli .
"""
# Pengembalian True untuk setiap baris yang merupakan duplikat, jika tidak False:
import pandas as pd
df = pd.read_csv('data.csv')
print(df.duplicated())

# Menghapus Duplikat
df.drop_duplicates(inplace = True)