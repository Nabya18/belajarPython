"""
Python Inheritance
1. Inheritance memungkinkan kita untuk mendefinisikan kelas yang mewarisi semua metode dan properti dari kelas lain.
2. Parent class adalah kelas yang diwarisi, disebut juga kelas dasar.
3. Child class adalah kelas yang mewarisi dari kelas lain, disebut juga kelas turunan.

1. Create a Parent Class: Kelas apa pun bisa menjadi kelas induk, jadi sintaksisnya sama dengan membuat kelas lainnya.
2. Create a Child Class
    a. Untuk membuat kelas yang mewarisi fungsionalitas dari kelas lain, kirimkan kelas induk sebagai parameter saat membuat kelas anak.
    b. Catatan: Gunakan pass kata kunci ketika Anda tidak ingin menambahkan properti atau metode lain ke kelas.
3. Add Fungsi __init__()
    a. Kita ingin menambahkan __init__() fungsi ke kelas anak (bukan kata passkunci).
    b. Catatan: Fungsi ini __init__() dipanggil secara otomatis setiap kali kelas digunakan untuk membuat objek baru.
    c. Saat Kita menambahkan __init__()fungsi tersebut, kelas anak tidak akan lagi mewarisi fungsi induknya __init__().
    d. Catatan:__init__() Fungsi anak mengambil alih warisan fungsi induk __init__().
    e. Untuk mempertahankan pewarisan fungsi induk __init__() , tambahkan panggilan ke fungsi induk __init__()
4. Fungsi super()
    super()fungsi yang akan membuat kelas anak mewarisi semua metode dan properti dari induknya:
    Dengan menggunakan super()fungsi tersebut, Kita tidak perlu menggunakan nama elemen induknya, secara otomatis akan mewarisi metode dan properti dari induknya.
5. Add Property
    Pada contoh di bawah, tahun 2019 harus berupa variabel, dan diteruskan ke Siswa kelas saat membuat objek siswa. Untuk melakukannya, tambahkan parameter lain di fungsi __init__()
6. Add Method
    Jika Kita menambahkan metode di kelas anak dengan nama yang sama dengan fungsi di kelas induk, pewarisan metode induk akan ditimpa.
"""

# Contoh Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Gunakan kelas Person untuk membuat objek, lalu jalankan metode printname:

x = Person("John", "Doe")
x.printname()

# Contoh Create a Child Class
# class Student(Person):
#   pass
# x = Student("Mike", "Olsen") # Gunakan Studentkelas untuk membuat objek
# x.printname()

# Contoh: Tambahkan __init__()fungsi ke Studentkelas
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

# Fungsi super()
class Siswa(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    # Add Property
    self.graduationyear = year # menambahkan properti

  # Add Methode
  def welcome(self):
      print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Siswa("Mike", "Olsen", 2019)
x.welcome()