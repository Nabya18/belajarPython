"""
Pandas - Membersihkan Sel Kosong
    1. Sel kosong berpotensi memberikan hasil yang salah saat Kita menganalisis data.
    2. Sel kosong adalah nilai yang hilang.
    3. Pandas mengganti nilai yang hilang dengan NaN (Not a Number).
    4. Untuk mengganti nilai yang hilang, Kita dapat menggunakan metode fillna().
    5. Catatan: Secara default, dropna()metode ini mengembalikan DataFrame baru , dan tidak akan mengubah yang asli.
    6. Kita dapat menggunakan inplace = True argumen untuk mengubah DataFrame asli.

Ganti Nilai Kosong
    1. Cara lain untuk menangani sel kosong adalah dengan memasukkan nilai baru .
    2. Dengan cara ini Kita tidak perlu menghapus seluruh baris hanya karena beberapa sel kosong.
    3. Metode ini fillna()memungkinkan kita mengganti sel kosong dengan nilai

Ganti Hanya Untuk Kolom Tertentu
    1. Contoh di atas menggantikan semua sel kosong di seluruh Data Frame.
    2. Untuk hanya mengganti nilai kosong pada satu kolom, tentukan nama kolom untuk DataFrame

Ganti Menggunakan Mean, Median, atau Mode
    1. Cara umum untuk mengganti sel kosong adalah dengan menghitung nilai mean, median, atau mode kolom.
    2. Pandas menggunakan metode mean() median()dan mode()untuk menghitung nilai masing-masing untuk kolom tertentu
    3. Mean = nilai rata-rata (jumlah seluruh nilai dibagi banyaknya nilai).
    4. Median = nilai tengah (nilai yang muncul paling banyak).
    5. Mode = nilai yang muncul paling banyak.
"""
## Hapus baris
# Mengembalikan Data Frame baru tanpa sel kosong
import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

# Hapus semua baris dengan nilai NULL di data frame asal
import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())
"""
Catatan: Sekarang, dropna(inplace = True) TIDAK akan mengembalikan DataFrame baru, 
tetapi akan menghapus semua baris yang berisi nilai NULL dari DataFrame asli.
"""

## Ganti Nilai Kosong
# Ganti nilai NULL dengan angka 130
import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = False)

# Ganti nilai NULL pada kolom "Kalori" dengan angka 130
import pandas as pd

df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = False)

## Ganti Menggunakan Mean, Median, atau Mode
# Hitung MEAN, dan ganti nilai kosong dengan nilai tersebut
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = False)

# Hitung MEDIAN, dan ganti nilai kosong dengan nilai tersebut
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = False)

# Hitung MODE, dan ganti nilai kosong dengan nilai tersebut
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = False)