"""
Open File di Server

Asumsikan kita memiliki file berikut, yang terletak di folder yang sama dengan Python:
    demofile.txt

Untuk membuka file, gunakan fungsi bawaan open().
Fungsi ini open() => mengembalikan objek file, yang memiliki read() => metode untuk membaca konten file:
    f = open("demofile.txt", "r")
    print(f.read())

Buka file di lokasi berbeda:
    f = open("D:\\myfiles\welcome.txt", "r")
    print(f.read())

Secara default, read()metode ini mengembalikan seluruh teks, namun Kita juga dapat menentukan berapa banyak karakter yang ingin Kita kembalikan:
Kembalikan 5 karakter pertama file:
    f = open("demofile.txt", "r")
    print(f.read(5))

Baca Garis
Kita dapat mengembalikan satu baris dengan menggunakan readline() metode:

Baca satu baris file:
    f = open("demofile.txt", "r")
    print(f.readline())

Dengan menelepon readline()dua kali, Kita dapat membaca dua baris pertama:
Baca dua baris file:
    f = open("demofile.txt", "r")
    print(f.readline())
    print(f.readline())

Dengan mengulang baris-baris file, Kita dapat membaca keseluruhan file, baris demi baris:
Ulangi file baris demi baris:
    f = open("demofile.txt", "r")
    for x in f:
      print(x)

Tutup File
Merupakan praktik yang baik untuk selalu menutup file setelah Kita selesai melakukannya.
Tutup file setelah Kita selesai melakukannya:
    f = open("demofile.txt", "r")
    print(f.readline())
    f.close()

Catatan: Kita harus selalu menutup file Kita, dalam beberapa kasus, karena buffering, perubahan yang dilakukan pada file mungkin tidak terlihat sampai Kita menutup file tersebut.
"""