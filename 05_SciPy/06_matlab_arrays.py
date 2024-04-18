"""
Matlab Arrays
    1. Kita tahu bahwa NumPy memberi kita metode untuk menyimpan data dalam format yang dapat dibaca untuk Python.
    2. Namun SciPy juga memberi kita interoperabilitas dengan Matlab.

SciPy memberi kita modul scipy.io, yang memiliki fungsi untuk bekerja dengan array Matlab.

Mengekspor Data dalam Format Matlab
    1. Fungsinya savemat() memungkinkan kita mengekspor data dalam format Matlab.
    2. Metode ini mengambil parameter berikut:
        a. nama file - nama file untuk menyimpan data.
        b. mdict - kamus yang berisi data.
        c. do_compression - nilai boolean yang menentukan apakah hasilnya akan dikompres atau tidak. Bawaan Salah.

Impor Data dari Format Matlab
    1. Fungsi ini loadmat() memungkinkan kita mengimpor data dari file Matlab.
    2. Fungsi ini mengambil satu parameter yang diperlukan:
        nama file - nama file dari data yang disimpan.
    3. Ini akan mengembalikan array terstruktur yang kuncinya adalah nama variabel, dan nilai yang sesuai adalah nilai variabel.

Catatan: Kita dapat melihat bahwa array aslinya 1D, tetapi saat diekstraksi, array tersebut bertambah satu dimensi.
Untuk mengatasi hal ini kita dapat memberikan argumen tambahan squeeze_me=True:
"""
# Ekspor array berikut sebagai nama variabel "vec" ke file mat
from scipy import io
import numpy as np

arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})
"""
Catatan: Contoh di atas menyimpan nama file "arr.mat" di komputer Kita.
Untuk membuka file, lihat contoh "Impor Data dari Format Matlab" di bawah ini:
"""

# Impor data dari file mat
from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# Export:
io.savemat('arr.mat', {"vec": arr})

# Import:
mydata = io.loadmat('arr.mat')

print(mydata)
"""
Gunakan nama variabel "vec" untuk hanya menampilkan array dari data matlab
"""
print(mydata['vec'])

# Impor data dari file mat dan menghilangkan dimensi tambahan
# Import:
mydata = io.loadmat('arr.mat', squeeze_me=True)

print(mydata['vec'])