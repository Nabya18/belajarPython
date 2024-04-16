"""
Pandas - Analyzing DataFrames

Viewing the Data
    1. Salah satu metode yang paling banyak digunakan untuk mendapatkan gambaran singkat tentang DataFrame adalah head() metode.
    2. Metode ini head() mengembalikan header dan sejumlah baris tertentu, dimulai dari atas.
    3. Catatan: jika jumlah baris tidak ditentukan, head()metode ini akan mengembalikan 5 baris teratas.
    4. Ada juga tail() metode untuk melihat baris terakhir DataFrame.
    5. Metode ini tail() mengembalikan header dan sejumlah baris tertentu, dimulai dari bawah.

Info About the Data
    Objek DataFrames memiliki metode yang disebut info(), yang memberi Kita lebih banyak informasi tentang kumpulan data.

Null Values
    1. Metode ini info() juga memberi tahu kita berapa banyak nilai Non-Null yang ada di setiap kolom
    2. Nilai kosong, atau nilai Null, bisa berdampak buruk saat menganalisis data, dan Kita harus mempertimbangkan untuk menghapus baris dengan nilai kosong.
    3. Ini adalah langkah menuju apa yang disebut pembersihan data
"""
# Dapatkan ikhtisar singkat dengan mencetak 10 baris pertama DataFrame
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

# Cetak 5 baris pertama DataFrame
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())

## Info Tentang Data
print(df.info())