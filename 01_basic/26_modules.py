"""
Modul Python
    1. Anggaplah sebuah modul sama dengan pustaka kode.
    2. File yang berisi serangkaian fungsi yang ingin Anda sertakan dalam aplikasi Anda

1. Buat Modul: Untuk membuat modul cukup simpan kode yang Anda inginkan dalam file dengan ekstensi file .py
2. Gunakan Modul
    a. kita dapat menggunakan modul yang baru saja kita buat, dengan menggunakan import pernyataan
    b. Catatan: Saat menggunakan fungsi dari modul, gunakan sintaks: module_name.function_name .
3. Variabel dalam Modul: Modul dapat berisi fungsi, seperti yang telah dijelaskan, tetapi juga semua jenis variabel (array, dict, objek, dll)
4. Memberi Nama Modul
    a. Anda dapat memberi nama file modul sesuka Anda, tetapi file tersebut harus memiliki ekstensi file .py
    b. Memberi nama ulang Modul: Anda dapat membuat alias saat mengimpor modul, dengan menggunakan as kata kunci:
5. Modul Bawaan: Ada beberapa modul bawaan di Python, yang dapat Anda impor kapan pun Anda mau.
    Berikut dibawah contoh modul bawaan Python:
    Nama Modul      Kegunaan Modul
    os:             Modul untuk interaksi dengan sistem operasi, seperti mengakses variabel lingkungan, mengelola direktori dan file, dll.
    sys:            Modul untuk akses ke berbagai komponen yang terkait dengan interpreter Python itu sendiri, seperti argumen baris perintah, path modul, dan fungsi-fungsi sistem.
    math:           Modul untuk operasi matematika, seperti fungsi matematika dasar, fungsi trigonometri, logaritma, dll.
    random:         Modul untuk menghasilkan bilangan acak.
    datetime:       Modul untuk bekerja dengan tanggal dan waktu.
    json:           Modul untuk mengkodekan dan mendekodekan data JSON.
    re:             Modul untuk bekerja dengan ekspresi reguler (regular expressions).
    urllib:         Modul untuk mengakses URL.
    socket:         Modul untuk pemrograman jaringan, untuk membuat dan menggunakan soket.
    csv:            Modul untuk membaca dan menulis file CSV.
    pickle:         Modul untuk serialisasi dan deserialisasi objek Python.
    collections:    Modul yang menyediakan struktur data tambahan seperti namedtuple, deque, Counter, dll.
6. Menggunakan Fungsi dir()
    a. Ada fungsi bawaan untuk mencantumkan semua nama fungsi (atau nama variabel) dalam sebuah modul. Fungsi dir()
    b. Catatan: Fungsi dir() dapat digunakan pada semua modul, juga modul yang Anda buat sendiri.
7. Impor Dari Modul
    a. Anda dapat memilih untuk mengimpor hanya bagian dari modul, dengan menggunakan from kata kunci.
    b. Catatan: Saat mengimpor menggunakan from kata kunci, jangan gunakan nama modul saat mengacu pada elemen dalam modul. Contoh: person1["age"], bukan mymodule.person1["age"]
"""
## Buat Modul => Simpan kode ini dalam file bernamamymodule.py
def greeting(name):
  print("Hello, " + name)

## Gunakan Modul => Impor modul bernama mymodule, dan panggil fungsi greetings:
import mymodule

mymodule.greeting("Jonathan")

## Variabel dalam Modul
# Simpan kode ini di filemymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Impor modul bernama mymodule, dan akses kamus person1
import mymodule

a = mymodule.person1["age"]
print(a)

## Memberi Nama Modul
# Memberi nama ulang Modul => Buat alias untuk mymodule dipanggil mx
import mymodule as mx

a = mx.person1["age"]
print(a)

## Modul Bawaan
# Impor dan gunakan platfor mmodul
import platform

x = platform.system()
print(x)

## Menggunakan Fungsi dir()
# List semua nama yang ditentukan milik modul platform
import platform

x = dir(platform)
print(x)

## Impor Dari Modul
# Modul bernama mymodule memiliki satu fungsi dan satu dict
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Impor hanya kamus person1 dari modul
from mymodule import person1

print (person1["age"])

"""
Saat Anda menggunakan kata kunci from untuk mengimpor modul dalam Python, 
Anda membuat nama-nama yang didefinisikan dalam modul tersebut tersedia secara langsung di dalam ruang nama (namespace) saat ini. 
Ini berarti Anda tidak perlu menyertakan nama modul saat mengacu pada elemen dalam modul tersebut.

Misalnya, jika Anda mengimpor modul mymodule menggunakan sintaksis from, seperti ini:
    from mymodule import person1

Ini akan membuat person1 langsung tersedia di ruang nama saat ini, 
sehingga Anda dapat menggunakan person1 langsung, tanpa perlu menyertakan nama modulnya:
    person1["age"]

Ini mempermudah dan mempersingkat penulisan kode, dan juga membuat kode menjadi lebih bersih dan mudah dibaca. 
Namun, Anda harus berhati-hati agar tidak mengimpor terlalu banyak nama dari modul yang sama, karena ini dapat menyebabkan konflik nama dan mengurangi keterbacaan kode.
"""