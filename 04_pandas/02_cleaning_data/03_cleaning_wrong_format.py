"""
Pandas - Membersihkan Data dengan Format yang Salah

Data Formatnya Salah
    1. Sel dengan format data yang salah dapat menyulitkan, atau bahkan tidak mungkin, menganalisis data.
    2. Untuk memperbaikinya, Kita memiliki dua opsi: menghapus baris, atau mengonversi semua sel di kolom ke dalam format yang sama.

Ubah Menjadi Format yang Benar
    1. Mari kita coba mengubah semua sel di kolom 'Date' menjadi dates.
    2. Pandas punya to_datetime() metode untuk ini

Menghapus Baris
    1. Hasil dari konversi pada contoh di atas memberi kita nilai NaT (Not a Time), yang dapat ditangani sebagai nilai NULL,
    2. dan kita dapat menghapus baris tersebut dengan menggunakan dropna() metode tersebut.
"""
# Ubah seluruh kolom 'Date' menjadi format tanggal
import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())

# Hapus baris dengan nilai NULL di kolom 'Date'
df.dropna(subset=['Date'], inplace = True)