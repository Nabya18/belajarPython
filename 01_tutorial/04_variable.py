'''
1. Python tidak memiliki perintah untuk mendeklarasikan variabel.
2. Variabel tidak perlu dideklarasikan dengan tipe tertentu
3. dapat diubah tipenya setelah ditetapkan

Untuk menggunakan string dapat menggunakan single atau double quotes
namun harus seragam

Case sensitive => variable a dan variable A itu berbeda
'''

# contoh nomor 2
x = 5 # x is of type int
print(x)

# contoh nomor 3
x = "Sally" # x is now of type str
print(x)

# untuk tipe data yang lebih spesifik
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# untuk mengetahui tipe data
a = 5
b = "John"
print(type(a))
print(type(b))

print("/n====Penamaan Variable===/n")
'''
1. harus diawali dengan huruf atau karakter garis bawah
2. tidak boleh diawali dengan angka
3. hanya boleh berisi karakter alfanumerik dan garis bawah (Az, 0-9, dan _ )
4. tidak boleh berupa kata kunci Python apa pun

Nama Variable Multi Kata
1. Camel Case
2. Pascal case
3. Snake Case
'''

myVariableName = "Camel Case"
MyVariableName = "Pascal Case"
my_variable_name = "Snake Case"

print("/n====multiple variable===/n")
#1. Banyak Nilai ke Banyak Variabel
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#2. Satu Nilai untuk Banyak Variabel
x = y = z = "Orange"
print(x)
print(y)
print(z)

#3. Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("/n====Output Variables===/n")
x = "Python"
y = "is"
z = "awesome"
print("mencetak output variable terpisah = ", x, y, z)
print("menggabungkan nilai variable pada string = ", x + y + z)

x = 5
y = 10
print("menjumlahkan nilai variable pada integer = ", x + y)

print("/n====Global Variables===/n")
'''
1. dibuat di luar suatu fungsi (seperti pada semua contoh di atas) dikenal sebagai variabel global
2. dapat digunakan oleh semua orang, baik di dalam fungsi maupun di luar fungsi.
3. Jika membuat variabel dengan nama yang sama di dalam suatu fungsi, variabel ini akan bersifat lokal, dan hanya dapat digunakan di dalam fungsi tersebut.
4. Untuk membuat variabel global di dalam suatu fungsi, dapat menggunakan 'global' kata kunci.
5. gunakan 'global' kata kunci jika ingin mengubah variabel global di dalam suatu fungsi.
'''

# contoh variable di luar fungsi
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# contoh variable di dalam fungsi
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# contoh menggunakan global kata kunci
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# contoh merubahkan variable global kata kunci
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)