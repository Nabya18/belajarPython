"""
Pandas DataFrame adalah struktur data 2 dimensi, seperti array 2 dimensi, atau tabel dengan baris dan kolom.

Locate Row
    1. Seperti yang Kita lihat dari hasil di atas, DataFrame seperti tabel dengan baris dan kolom.
    2. PKita menggunakan locatribut untuk mengembalikan satu atau lebih baris tertentu

1. Named Indexes => Dengan index argumen tersebut, Kita dapat memberi nama indeks Kita sendiri.
2. Locate Named Indexes => Gunakan indeks bernama dalam loc atribut untuk mengembalikan baris tertentu.
3. Load Files Into a DataFrame => Jika kumpulan data Kita disimpan dalam sebuah file, Pandas dapat memuatnya ke dalam DataFrame.
"""
# Buat DataFrame Pandas sederhana
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
print(df.loc[0]) # Kembalikan baris pertama
print(df.loc[[0, 1]]) # Kembalikan baris pertama dan kedua
"""
Catatan: Saat menggunakan [], hasilnya adalah Pandas DataFrame .
"""

# Tambahkan daftar nama untuk memberi nama pada setiap baris
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
print(df.loc["day2"]) # Kembalikan baris dengan label "day2"

## Muat file yang dipisahkan koma (file CSV) ke dalam DataFrame
# import pandas as pd
#
# df = pd.read_csv('data.csv')
#
# print(df)