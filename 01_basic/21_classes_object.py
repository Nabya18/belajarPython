"""
Kelas/Objek Python
    1. Python adalah bahasa pemrograman berorientasi objek.
    2. Hampir semua yang ada di Python adalah sebuah objek, dengan properti dan metodenya.
    3. Kelas seperti konstruktor objek, atau "cetak biru" untuk membuat objek.

1. Buat Kelas: Untuk membuat kelas, gunakan kata kunci class
2. Buat Objek: Untuk membuat objek, Akses nama kelas
3. Fungsi __init__()
    a. Semua kelas memiliki fungsi yang disebut __init__(), yang selalu dijalankan saat kelas dimulai.
    b. Gunakan fungsi __init__() untuk menetapkan nilai pada properti objek, atau operasi lain yang perlu dilakukan saat objek dibuat
    c. Catatan: Fungsi ini __init__()dipanggil secara otomatis setiap kali kelas digunakan untuk membuat objek baru.
4. Fungsi __str__()
    a. Fungsi __str__() mengontrol apa yang harus dikembalikan ketika objek kelas direpresentasikan sebagai string.
    b. Jika fungsi __str__() tidak disetel, representasi string objek akan dikembalikan
5. Metode Objek
  a. Objek juga bisa berisi metode. Metode dalam objek adalah fungsi yang dimiliki objek tersebut.
  b. Catatan: Parameter selfadalah referensi ke instance kelas saat ini, dan digunakan untuk mengakses variabel milik kelas tersebut.
6. Parameter self
  a. Parameter selfadalah referensi ke instance kelas saat ini, dan digunakan untuk mengakses variabel milik kelas tersebut.
  b. Itu tidak harus diberi nama self, Kita bisa menyebutnya apa pun yang Kita suka, tetapi itu harus menjadi parameter pertama dari fungsi apa pun di kelas:
7. Ubah Properti Objek
    contoh => p1.age = 40
8. Hapus Properti Objek: dapat menghapus properti pada objek dengan menggunakan delkata kunci
    contoh => del p1.age
9. Hapus Objek: dapat menghapus objek dengan menggunakan delkata kunci
    contoh => del p1
10. The pass Statement
    class definisi tidak boleh kosong, tetapi jika karena alasan tertentu Kita memiliki class definisi tanpa konten, masukkan Pass untuk menghindari kesalahan.
"""

# Buat kelas bernama MyClass, dengan properti bernama x:
class MyClass:
  x = 5

# menggunakan kelas bernama MyClass untuk membuat objek
p1 = MyClass()
print(p1.x)

# menggunakan fungsi __init__() untuk menetapkan nilai nama dan usia:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Representasi string suatu objek DENGAN fungsi __str__():
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# Metode objek: Masukkan fungsi yang mencetak salam, dan jalankan pada objek p1:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Gunakan kata mysillyobject dan abc alih-alih self :
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# contoh Pass Statement
class Person:
  pass