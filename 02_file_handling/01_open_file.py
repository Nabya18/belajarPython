"""
Penanganan file adalah bagian penting dari aplikasi web apa pun.
Python memiliki beberapa fungsi untuk membuat, membaca, memperbarui, dan menghapus file.

Penanganan Berkas
1. Fungsi utama untuk bekerja dengan file dengan Python adalah fungsinya open().
2. Fungsi ini open() => mengambil dua parameter; nama file , dan mode .

Ada empat metode (mode) berbeda untuk membuka file:
"r"- Read - Nilai default. Membuka file untuk dibaca, error jika file tidak ada
"a"- Add - Membuka file untuk ditambahkan, membuat file jika tidak ada
"w"- Write - Membuka file untuk ditulis, membuat file jika tidak ada
"x"- Create - Membuat file yang ditentukan, mengembalikan kesalahan jika file tersebut ada

Selain itu Kita dapat menentukan apakah file harus ditangani sebagai mode biner atau teks
"t"- Teks - Nilai default. Modus teks
"b"- Biner - Mode biner (misalnya gambar)

Untuk membuka file untuk dibaca, cukup tentukan nama file:
    f = open("demofile.txt")

Kode di atas sama dengan:
    f = open("demofile.txt", "rt")

Karena "r" untuk membaca dan "t"teks adalah nilai default, Kita tidak perlu menentukannya.

Catatan: Pastikan file tersebut ada, jika tidak Kita akan mendapatkan kesalahan.
"""