"""
Create ufunc
1. Untuk membuat ufunc Anda sendiri, Anda harus mendefinisikan suatu fungsi,
2. seperti yang Anda lakukan dengan fungsi normal dengan Python,
3. lalu Anda menambahkannya ke perpustakaan ufunc NumPy Anda dengan frompyfunc()metode tersebut.
4. Metode ini frompyfunc() mengambil argumen berikut:
    function-   nama fungsinya.
    inputs-     jumlah argumen masukan (array).
    outputs-    jumlah array keluaran.

Ufunc harus kembali <class 'numpy.ufunc'>.c
Jika bukan ufunc, ia akan mengembalikan tipe lain, seperti fungsi NumPy bawaan ini untuk menggabungkan dua atau lebih array.
Untuk menguji apakah fungsinya adalah ufunc dalam pernyataan if, gunakan nilainya numpy.ufunc (atau np.ufuncjika Anda menggunakan np sebagai alias untuk numpy)
"""
# Buat ufunc Anda sendiri untuk tambahan
import numpy as np

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

"""
Kode ini menggunakan fungsi np.frompyfunc() dari NumPy untuk mengonversi fungsi Python myadd() menjadi sebuah ufunc (universal function) NumPy. 
Sebuah ufunc adalah fungsi yang beroperasi pada array NumPy elemen demi elemen, memungkinkan operasi yang cepat dan efisien pada array.

Dalam kasus ini, fungsi Python myadd() sederhana dan hanya menambahkan dua bilangan bersama-sama. 
Setelah diubah menjadi ufunc NumPy, ia mampu beroperasi pada array NumPy secara efisien, melakukan penambahan elemen demi elemen.

Pada baris terakhir, kita menggunakan ufunc yang telah dibuat untuk menjumlahkan dua array: [1, 2, 3, 4] dan [5, 6, 7, 8]. 
Hasilnya adalah sebuah array NumPy yang berisi hasil penjumlahan setiap pasangan elemen yang sesuai dari kedua array tersebut.

Jadi, hasil yang dicetak adalah hasil penjumlahan dari kedua array tersebut, yaitu [6, 8, 10, 12].

Dalam konteks aplikasi, penggunaan np.frompyfunc() ini memungkinkan kita untuk membuat fungsi Python sederhana dan kemudian menggunakannya pada array NumPy dengan efisien, 
meningkatkan kinerja dan fleksibilitas dalam pemrograman dengan NumPy.
"""

# Periksa apakah suatu fungsi adalah ufunc
import numpy as np

print(type(np.add))

# Periksa jenis fungsi lain: concatenate()
import numpy as np

print(type(np.concatenate))

# Gunakan pernyataan if untuk memeriksa apakah fungsinya adalah ufunc atau bukan
import numpy as np

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')