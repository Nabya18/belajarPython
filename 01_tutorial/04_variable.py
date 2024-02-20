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