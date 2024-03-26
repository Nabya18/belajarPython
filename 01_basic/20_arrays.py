"""
Catatan: Python tidak memiliki dukungan bawaan untuk Array, namun List Python dapat digunakan sebagai gantinya.
untuk bekerja dengan array dengan Python, Kita harus mengimpor dict, seperti dict NumPy.

Array adalah variabel khusus yang dapat menampung lebih dari satu nilai dalam satu waktu.
    1. Array digunakan untuk menyimpan banyak nilai dalam satu variabel
    2. Kita dapat mengakses nilai tersebut dengan mengacu pada nomor indeks.
    3. Panjang array selalu lebih panjang satu dari indeks array tertinggi.

1. Perulangan Elemen Array: dapat menggunakan for inloop untuk mengulang semua elemen array.
2. Menambahkan Elemen Array: menggunakan append()metode ini untuk menambahkan elemen ke array.
3. Menghapus Elemen Array: menggunakan pop()metode ini untuk menghapus elemen dari array.
4. menghapus kemunculan pertama dari nilai yang ditentukan: menggunakan remove() metode ini untuk menghapus elemen dari array.

Python memiliki serangkaian metode bawaan yang dapat Anda gunakan pada list/array.
    Method	            Description
    append()	        Menambahkan elemen di akhir list
    clear()	            Menghapus semua elemen dari list
    copy()	            Mengembalikan salinan list
    count()	            Mengembalikan jumlah elemen dengan nilai yang ditentukan
    extend()	        Menambahkan elemen list (atau apa pun yang dapat diubah), ke akhir list saat ini
    index()	            Mengembalikan indeks elemen pertama dengan nilai yang ditentukan
    insert()	        Menambahkan elemen pada posisi yang ditentukan
    pop()	            Menghapus elemen pada posisi yang ditentukan
    remove()	        Menghapus item dengan nilai yang ditentukan
    reverse()	        Membalikkan urutan list
    sort()	            Mengurutkan list
"""

# contoh array
cars = ["Ford", "Volvo", "BMW"]

# Dapatkan nilai item array pertama
a = cars[0]

# mengubah nilai item array pertama
cars[0] = "Toyota"

# Mengembalikan jumlah elemen dalam cars array
y = len(cars)

# Perulangan array
for x in cars:
  print(x)

# Menambahkan Elemen Array
cars.append("Honda")

# Menghapus Elemen Array: pop()
cars.pop(1)

# Menghapus Elemen Array: remove()
cars.remove("Volvo")