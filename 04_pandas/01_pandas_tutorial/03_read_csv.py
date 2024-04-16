"""
Read CSV Files
    1. Cara sederhana untuk menyimpan kumpulan data besar adalah dengan menggunakan file CSV (file yang dipisahkan koma).
    2. File CSV berisi teks biasa dan merupakan format terkenal yang dapat dibaca oleh semua orang termasuk Pandas.
    3. Tip: gunakan to_string() untuk mencetak seluruh DataFrame.
    4. Jika Kita memiliki DataFrame besar dengan banyak baris, Pandas hanya akan mengembalikan 5 baris pertama, dan 5 baris terakhir

max_rows
    1. Jumlah baris yang dikembalikan ditentukan dalam pengaturan opsi Pandas.
    2. Kita dapat memeriksa baris maksimum sistem Kita dengan pd.options.display.max_rows pernyataan tersebut.
"""
## Muat CSV ke dalam DataFrame
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) # Cetak seluruh DataFrame

## Cetak DataFrame tanpa to_string() metode
import pandas as pd

df = pd.read_csv('data.csv')

print(df) # cetak 5 baris pertama dan 5 baris terakhir

## Cek baris maksimum
import pandas as pd

print(pd.options.display.max_rows)
"""
Di sistem, angkanya adalah 60, yang berarti jika DataFrame berisi lebih dari 60 baris, 
print(df) pernyataan tersebut hanya akan mengembalikan header dan 5 baris pertama dan terakhir.

Kita dapat mengubah nomor baris maksimum dengan pernyataan yang sama.
"""

## Tingkatkan jumlah baris maksimum untuk menampilkan seluruh DataFrame
import pandas as pd

pd.options.display.max_rows = 9999 # Menampilkan seluruh DataFrame

df = pd.read_csv('data.csv')

print(df)