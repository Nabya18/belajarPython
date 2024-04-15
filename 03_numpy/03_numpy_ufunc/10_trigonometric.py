"""
Fungsi Trigonometri NumPy
    NumPy menyediakan ufuncs sin(), cos()yang tan()mengambil nilai dalam radian dan menghasilkan nilai sin, cos, dan tan yang sesuai.

Ubah Derajat Menjadi Radian
    Secara default, semua fungsi trigonometri menggunakan radian sebagai parameter,
    tetapi kita juga dapat mengonversi radian menjadi derajat dan sebaliknya di NumPy.
    Catatan: nilai radian adalah pi/180 * nilai_derajat.

Radian ke Derajat
    Untuk mengonversi sudut radian menjadi derajat, kalikan nilai dengan 180/pi.
    NumPy menyediakan nilai pi yang kita butuhkan untuk melakukan konversi.

Menemukan Sudut
    Mencari sudut dari nilai sinus, cos, tan. Misal invers sin, cos dan tan (arcsin, arccos, arctan).
    NumPy menyediakan ufuncs arcsin(), arccos()dan arctan()itu menghasilkan nilai radian untuk nilai sin, cos, dan tan terkait yang diberikan.

sisi miring
    Menemukan sisi miring menggunakan teorema pythagoras di NumPy.
    NumPy menyediakan hypot()fungsi yang mengambil nilai alas dan tegak lurus serta menghasilkan sisi miring berdasarkan teorema pythagoras.
"""
## Fungsi trigonometri
# Temukan nilai sinus PI/2
import numpy as np

x = np.sin(np.pi/2)

print(x)

# Temukan nilai sinus untuk semua nilai di arr
import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)
"""
Kode yang Kita pilih menghitung nilai sinus dari beberapa sudut yang diberikan dalam radian dan mencetak hasilnya. 
Berikut adalah penjelasan lebih rinci:  
np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5]): Membuat array numpy yang berisi sudut dalam radian. 
Nilai np.pi adalah konstanta π (pi), dan np.pi/2, np.pi/3, np.pi/4, dan np.pi/5 
masing-masing adalah π/2, π/3, π/4, dan π/5 radian.  

np.sin(arr): Menghitung nilai sinus dari setiap sudut dalam array tersebut. 
Fungsi sinus adalah fungsi trigonometri yang menghasilkan rasio antara sisi berlawanan dengan sudut dalam segitiga siku-siku terhadap hipotenusa.  

print(x): Mencetak hasil perhitungan tersebut. 
 
Jadi, kode tersebut mencetak nilai sinus dari π/2, π/3, π/4, dan π/5 radian. 
Nilai-nilai ini dihitung menggunakan fungsi np.sin(), yang merupakan fungsi trigonometri sinus dalam numpy.  
Berikut adalah nilai-nilai yang dihasilkan:  
    np.sin(np.pi/2) menghasilkan 1.0 karena sinus dari π/2 radian adalah 1.
    np.sin(np.pi/3) menghasilkan 0.86602540378 karena sinus dari π/3 radian adalah √3/2, yang kira-kira sama dengan 0.866.
    np.sin(np.pi/4) menghasilkan 0.70710678118 karena sinus dari π/4 radian adalah 1/√2, yang kira-kira sama dengan 0.707.
    np.sin(np.pi/5) menghasilkan 0.58778525229 karena sinus dari π/5 radian adalah √(5 - √5)/8, yang kira-kira sama dengan 0.588.

Jadi, output dari kode tersebut adalah array [1.0, 0.86602540378, 0.70710678118, 0.58778525229]
"""

## Ubah Derajat Menjadi Radian
# Ubah semua nilai dalam array arr berikut menjadi radian
import numpy as np

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)

## Radian ke Derajat
# Ubah semua nilai dalam array arr berikut menjadi derajat
import numpy as np

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)

## Menemukan Sudut
# Temukan sudut 1,0
import numpy as np

x = np.arcsin(1.0)

print(x)

## Sudut Setiap Nilai dalam Array
# Temukan sudut untuk semua nilai dalam array
import numpy as np

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)

## Sisi Miring
# Temukan sisi miring untuk 4 dan 3
import numpy as np

base = 3
perp = 4

x = np.hypot(base, perp)

print(x)