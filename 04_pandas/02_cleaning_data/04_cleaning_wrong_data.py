"""
Pandas - Memperbaiki Data yang Salah
Data yang Salah
    1. Data yang salah bisa berupa data yang hilang, data dalam format yang salah, atau data yang tidak relevan.
    2. Data yang salah dapat menyebabkan hasil analisis yang salah, dan itu sangat penting untuk memperbaikinya.
    3. Pandas menyediakan beberapa metode untuk memperbaiki data yang salah.

1. Untuk kumpulan data kecil Kita mungkin dapat mengganti data yang salah satu per satu, namun tidak untuk kumpulan data besar.
2. Untuk mengganti data yang salah dengan kumpulan data yang lebih besar, Kita dapat membuat beberapa aturan,
    misalnya menetapkan beberapa batasan untuk nilai hukum, dan mengganti nilai apa pun yang berada di luar batasan tersebut.

Menghapus Baris
    1. Cara lain untuk menangani data yang salah adalah dengan menghapus baris yang berisi data yang salah.
    2. Dengan cara ini Kita tidak perlu mencari tahu apa yang harus menggantikannya, dan ada kemungkinan Kita tidak memerlukannya untuk melakukan analisis.
"""
## Mengganti Nilai
# Tetapkan "Durasi" = 45 di baris 7
import pandas as pd
df = pd.read_csv('data.csv')
df.loc[150, 'Duration'] = 15

# Ulangi semua nilai di kolom "Durasi".
# Jika nilainya lebih tinggi dari 120, setel ke 120
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

# Hapus baris yang "Durasi" lebih tinggi dari 120
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace = True)