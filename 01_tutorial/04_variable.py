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