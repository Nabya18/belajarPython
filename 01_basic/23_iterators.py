"""
Iterator Python
1. Iterator adalah objek yang berisi sejumlah nilai yang dapat dihitung.
2. Iterator adalah objek yang dapat diiterasi, artinya Kita dapat melintasi semua nilai.
3. Secara teknis, dalam Python, iterator adalah objek yang mengimplementasikan protokol iterator, yang terdiri dari metode __iter__() dan __next__().

1. Iterator vs Iterable
    a. List, tuple, dict, dan sets semuanya merupakan iterable object.
    b. Mereka adalah wadah yang dapat diubah dimana Kita bisa mendapatkan iteratornya.
    c. Semua objek ini memiliki iter() metode yang digunakan untuk mendapatkan iterator
    d. Bahkan string adalah iterable object, dan dapat mengembalikan sebuah iterator

2. Perulangan Melalui Iterator
    a. dapat menggunakan forloop untuk melakukan iterasi melalui iterable object
    b. Perulangan for sebenarnya membuat objek iterator dan mengeksekusi metode next() untuk setiap perulangan.

3. Membuat Iterator
    a. Untuk membuat objek/kelas sebagai iterator, Kita harus mengimplementasikan metode __iter__()dan __next__()objek Kita.
    b. Seperti yang telah Kita pelajari di bab Kelas/Objek Python , semua kelas memiliki fungsi yang disebut __init__(), yang memungkinkan Kita melakukan inisialisasi saat objek dibuat.
    c. Metode ini __iter__()bertindak serupa, Kita dapat melakukan operasi (menginisialisasi, dll.), tetapi harus selalu mengembalikan objek iterator itu sendiri.
    d. Metode ini __next__()juga memungkinkan Kita melakukan operasi, dan harus mengembalikan item berikutnya dalam urutan.

4. Menghentikan Iterator
    a. Contoh di 'Membuat Iterator' akan berlanjut selamanya jika Kita memiliki cukup pernyataan next(), atau jika digunakan dalam satu for perulangan.
    b. Untuk mencegah iterasi berlangsung selamanya, kita dapat menggunakan Stop Iteration pernyataan tersebut.
    c. Dalam __next__()metode ini, kita dapat menambahkan kondisi penghentian untuk memunculkan kesalahan jika iterasi dilakukan beberapa kali
"""
## 1. Iterator vs Iterable
# Kembalikan iterator dari Tuple, dan cetak setiap nilai
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# String juga merupakan iterable object, berisi rangkaian karakter
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

## 2. Perulangan Melalui Iterator
# Iterasi nilai Tuple
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# Ulangi karakter string
mystr = "banana"

for x in mystr:
  print(x)

## Membuat Iterator
# Buat iterator yang mengembalikan angka, dimulai dengan 1, dan setiap urutan akan bertambah satu (mengembalikan 1,2,3,4,5 dll.)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

## Menghentikan Iterator
# Berhenti setelah 20 iterasi
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)