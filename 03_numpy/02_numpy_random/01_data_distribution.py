"""
Random data distribution
    1. Distribusi Data adalah daftar semua nilai yang mungkin, dan seberapa sering setiap nilai muncul.
    2. Daftar tersebut penting ketika bekerja dengan statistik dan ilmu data.
    3. Modul acak menawarkan metode yang mengembalikan distribusi data yang dihasilkan secara acak.

Random data distribution => sekumpulan bilangan acak yang mengikuti probability density function tertentu .
Probability Density Function: Fungsi yang menggambarkan probabilitas berkelanjutan. yaitu probabilitas semua nilai dalam array.
    1. Kita dapat menghasilkan angka acak berdasarkan probabilitas yang ditentukan menggunakan choice()metode modul random.
    2. Metode ini choice()memungkinkan kita menentukan probabilitas untuk setiap nilai.
    3. Probabilitas ditentukan oleh angka antara 0 dan 1, dimana 0 berarti nilai tidak akan pernah muncul dan 1 berarti nilai akan selalu terjadi.
    4. Jumlah semua angka probabilitas harus 1.

Kita dapat mengembalikan array dalam bentuk dan ukuran apa pun dengan menentukan bentuk di sizeparameter.
"""
# Hasilkan array 1-D yang berisi 100 nilai, dengan setiap nilai harus 3, 5, 7, atau 9.
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)
"""
Probabilitas nilai menjadi 3 ditetapkan menjadi 0,1
Probabilitas nilai menjadi 5 ditetapkan menjadi 0,3
Probabilitas nilai menjadi 7 ditetapkan menjadi 0,6
Probabilitas nilai menjadi 9 ditetapkan menjadi 0
"""

# Contoh yang sama seperti di atas, tetapi mengembalikan array 2D dengan 3 baris, masing-masing berisi 5 nilai.
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)