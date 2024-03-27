"""
Polimorfisme Python
    Kata "polimorfisme" berarti "banyak bentuk", dan dalam pemrograman mengacu pada metode/fungsi/operator dengan nama yang sama yang dapat dieksekusi pada banyak objek atau kelas.

1. Polimorfisme Fungsi: Contoh fungsi Python yang dapat digunakan pada objek berbeda adalah fungsi len()
    a. String: string len() mengembalikan jumlah karakter
    b. Tuple: tupel len() mengembalikan jumlah item dalam tupel
    c. Dictionary: dictionary len() mengembalikan jumlah pasangan kunci/nilai dalam kamus

2. Polimorfisme Kelas
    - Polimorfisme sering digunakan dalam metode Kelas, dimana kita dapat memiliki beberapa kelas dengan nama metode yang sama.
    - Misalnya, kita mempunyai tiga kelas: Car, Boat, dan Plane, dan semuanya memiliki metode yang disebut move()
    - Lihatlah perulangan for di akhir contoh. Karena polimorfisme kita dapat menjalankan metode yang sama untuk ketiga kelas.

3. Polimorfisme Kelas Inheritance
    - Kita dapat menggunakan polimorfisme di kelas inheritance dengan nama yang sama dengan kelas parent
    - Jika kita menggunakan contoh di atas dan membuat kelas induk bernama Vehicle, dan menjadikan Car, Boat, Plane kelas anak dari Vehicle,
    - kelas anak tersebut akan mewarisi Vehicle metode tersebut, namun dapat menimpanya
    - Kelas anak mewarisi properti dan metode dari kelas induk.
    - Pada contoh di bawah Kita dapat melihat bahwa kelasnya Carkosong, tetapi ia mewarisi brand, model, dan move() from Vehicle.
    - Kelas Boatand Planejuga mewarisi brand, model, dan move()from Vehicle, namun keduanya mengesampingkan move() metode tersebut.
    - Karena polimorfisme kita dapat menjalankan metode yang sama untuk semua kelas.
"""
## Polimorfisme Fungsi
# String
x = "Hello World!"
print(len(x))

# Tuple
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))

## Polimorfisme Kelas
# Kelas berbeda dengan metode yang sama
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):  #dapat menjalankan metode yang sama untuk ketiga kelas.
  x.move()

## Polimorfisme Kelas Inheritance
# Buat sebuah kelas bernama Vehicledan buatlah Car, Boat, Plane kelas anak dari Vehicle
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

"""
Kelas Boat dan Plane mewarisi sifat-sifat (properties) dan perilaku (behavior) dari kelas Vehicle karena keduanya adalah subkelas dari Vehicle. 
Dalam warisan (inheritance), subkelas akan mewarisi metode dan atribut dari kelas induknya, kecuali jika metode atau atribut tersebut di-override di dalam subkelas.

Dalam contoh yang diberikan, kelas Boat dan Plane tidak hanya mewarisi atribut brand dan model dari kelas Vehicle, tetapi juga mewarisi metode move(). 
Namun, keduanya meng-override metode move() yang telah didefinisikan di kelas Vehicle.

Ketika Kita membuat objek Car, Boat, atau Plane, Kita sebenarnya membuat objek dari subkelas tersebut. 
Oleh karena itu, ketika Kita memanggil metode move() pada objek-objek tersebut, Python akan mencari metode move() di kelas tersebut terlebih dahulu. 
Jika metode tersebut tidak ditemukan, Python akan mencari di kelas induknya. 
Ini adalah konsep yang disebut dengan "method overriding", di mana subkelas dapat memiliki implementasi yang berbeda untuk metode yang sama seperti yang dimiliki oleh kelas induknya.
"""