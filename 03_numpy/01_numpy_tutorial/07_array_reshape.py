"""
Array Reshape => mengubah bentuk array
Dengan membentuk kembali kita dapat menambah atau menghapus dimensi atau mengubah jumlah elemen di setiap dimensi.

Bisakah Kita Membentuk Kembali Menjadi Bentuk Apa Pun?
    Ya, selama elemen yang diperlukan untuk membentuk kembali sama di kedua bentuk.
    Kita dapat membentuk kembali array 1D 8 elemen menjadi 4 elemen dalam array 2D 2 baris tetapi kita tidak dapat membentuknya kembali menjadi array 2D 3 elemen 3 baris karena memerlukan 3x3 = 9 elemen.

Unknown Dimension
    1. Kita diperbolehkan memiliki satu dimensi yang "tidak diketahui".
    2. Artinya Kita tidak perlu menentukan angka pasti untuk salah satu dimensi dalam metode reshape.
    3. Berikan -1sebagai nilainya, dan NumPy akan menghitung angka ini untuk Kita.

Flattening array
    1. mengubah array multidimensi menjadi array 1D.
    2. Kita bisa menggunakannya reshape(-1)untuk melakukan hal ini.

Catatan: Ada banyak fungsi untuk mengubah bentuk array di numpy flatten, ravel dan juga untuk mengatur ulang elemen rot90, flip, fliplr, flipud dll. Fungsi ini termasuk dalam bagian Intermediate hingga Advanced dari numpy.
"""
## Bentuk Ulang Dari 1-D ke 2-D
# Ubah array 1-D berikut dengan 12 elemen menjadi array 2-D.
# Dimensi terluar akan memiliki 4 array, masing-masing dengan 3 elemen
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
"""
Ini mengubah array 1-D dengan 12 elemen menjadi array 2-D dengan 4 baris dan 3 kolom.
"""


## Bentuk Ulang Dari 1-D ke 3-D
# Ubah array 1-D berikut dengan 12 elemen menjadi array 3-D.
# Dimensi terluar akan memiliki 2 array yang berisi 3 array, masing-masing dengan 2 elemen
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)
"""
Ini mengubah array 1-D dengan 12 elemen menjadi array 3-D dengan 2 sub-array yang masing-masing memiliki 3 sub-array dengan 2 elemen.
"""


## Mengembalikan Salin atau Lihat?
# Periksa apakah array yang dikembalikan adalah salinan atau tampilan
# Contoh di bawah mengembalikan array asli, jadi ini adalah tampilan.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)
"""
Ini mencetak array asli, menunjukkan bahwa reshape hanya membuat tampilan baru dari array aslinya.
Dalam hal ini, kita mengkonfirmasi apakah array yang dikembalikan dari reshape adalah salinan array asli atau hanya tampilan.
Karena base dari array yang direshape sama dengan array asli, ini menunjukkan bahwa reshape hanya membuat tampilan baru dari array aslinya.
"""


## Dimensi Tidak Diketahui
# Ubah array 1D dengan 8 elemen menjadi array 3D dengan elemen 2x2
# Catatan: Kita tidak dapat meneruskan -1 ke lebih dari satu dimensi.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)
"""
Dalam contoh ini, nilai -1 digunakan untuk dimensi ketiga, yang menyebabkan NumPy menyesuaikan ukuran dimensi ketiga secara otomatis agar total elemen tetap sama.
Di sini, kita menggunakan -1 sebagai parameter reshape pada dimensi ketiga.
Ini menginstruksikan NumPy untuk menyesuaikan ukuran dimensi ketiga secara otomatis agar total elemen tetap sama dengan array asli.
Sehingga, kita mendapatkan array 3-D dengan 2 sub-array, masing-masing memiliki 2 sub-array yang masing-masing memiliki 2 elemen.
"""


## Flattening array
# Ubah array menjadi array 1D
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)
"""
Ini mengubah array 2-D menjadi array 1-D. -1 dalam reshape menunjukkan bahwa NumPy harus menghitung ukuran dimensi yang sesuai untuk array 1-D berdasarkan jumlah elemen array yang asli.
Ini menyebabkan NumPy menghitung ukuran dimensi yang sesuai untuk array 1-D berdasarkan jumlah elemen array asli.
Sehingga, array 2-D dengan 2 baris dan 3 kolom diubah menjadi array 1-D.
"""