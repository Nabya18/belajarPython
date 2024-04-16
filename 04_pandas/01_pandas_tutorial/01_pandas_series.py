"""
1. Series Pandas seperti kolom dalam tabel.
2. Ini adalah array satu dimensi yang menyimpan data jenis apa pun.

Label
    1. Jika tidak ada hal lain yang ditentukan, nilai diberi label dengan nomor indeksnya.
    2. Nilai pertama memiliki indeks 0, nilai kedua memiliki indeks 1 dan seterusnya.
    3. Label ini dapat digunakan untuk mengakses nilai tertentu.

Buat Label
    1. Dengan index argumen tersebut, Kita dapat memberi nama label Kita sendiri.
    2. Ketika Kita telah membuat label, Kita dapat mengakses suatu item dengan mengacu pada label tersebut.

Objek key/value sebagai Series
    1. Kita juga dapat menggunakan objek key/value, seperti dict, saat membuat Series.
    2. Catatan: key dict menjadi label.
    3. Untuk memilih hanya beberapa item dalam kamus, gunakan argumen index dan tentukan hanya item yang ingin Kita sertakan dalam Seri.

Data Frames
    1. Kumpulan data di Pandas biasanya berupa tabel multidimensi, yang disebut DataFrames.
    2. Series itu seperti kolom, DataFrame adalah keseluruhan tabel.
"""
## Buat Series Pandas sederhana dari daftar
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0]) # Kembalikan nilai pertama Series

## Buat label Kita sendiri
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print(myvar["y"]) # Kembalikan nilai dengan label "y"

## Objek key/value sebagai Series
# Buat Series Pandas sederhana dari dict
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# Buat Series hanya menggunakan data dari "day1" dan "day2"
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

## Data Frames
# Buat DataFrame dari dua series
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)