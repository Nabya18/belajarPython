"""
Tuple adalah koleksi yang terurut dan tidak dapat diubah .
    Karakteristik Tuple:
    1. Tuple ditulis dengan ()
    2. diurutkan => memiliki urutan yang ditentukan, dan urutan itu tidak akan berubah.
    3. Tidak dapat diubah => Tidak dapat mengubah, menambah, dan menghapus item dalam tuple setelah dibuat.
    4. memungkinkan nilai duplikat => tuple dapat memiliki item dengan nilai yang sama
    5. diindeks, item pertama memiliki indeks [0], item kedua memiliki indeks, [1]dll.
    6. item dapat berupa tipe data apa pun
    7. dapat menggunakan tuple() constructor
    8. immutable

1. Access Tuples => menggunakan indexing (seperti list)
2. Update Tuples => harus diubah menjadi list terlebih dahulu baru konversi kembali ke tuple
    - Saat membuat tupel dengan hanya satu item, ingatlah untuk menyertakan koma setelah item, jika tidak maka tidak akan diidentifikasi sebagai tupel.
    - menghapus tuple dapat menggunakan solusi yang sama
3. Unpack Tuples
    - Mengekstrak nilai kembali ke dalam variabel
    - Jumlah variabel harus sesuai dengan jumlah nilai dalam tupel, jika tidak, harus menggunakan tanda bintang untuk mengumpulkan nilai yang tersisa sebagai daftar.
    - tanda bintang hanya di salah satu variabel
4. Loop Tuples
    a. For Loop
    b. While loop
        -  mulai dari 0 dan ulangi item tupel dengan mengacu pada indeksnya.
        -  Ingatlah untuk meningkatkan indeks sebesar 1 setelah setiap iterasi.
5. Join Tuples
    - menggunakan operator +
    - menggunakan operator * => untuk menggandakan
6. Tupple Methods
    Method	    Description
    count()	    Mengembalikan berapa kali nilai tertentu muncul dalam tupel
    index()	    Mencari tupel untuk nilai tertentu dan mengembalikan posisi di mana nilai itu ditemukan
"""

## Contoh Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# membuat tuple dengan 1 item
thistuple = ("apple",) #harus ada koma
thisstring = ("apple")
print(type(thistuple))
print(type(thisstring))

# tuple dengan konstruktor
thistuple1 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple1)

## Update Tuple
# Ubah Nilai
x = ("apple", "banana", "cherry")
y = list(x) # Rubah ke list
y[1] = "kiwi"
x = tuple(y) # rubah ke tuple

print(x)

# Add Item
thistuple2 = ("apple", "banana", "cherry")
y = list(thistuple2)
y.append("orange")
thistuple2 = tuple(y)

# Remove Item di Tuple
thistuple3 = ("apple", "banana", "cherry")
y = list(thistuple3)
y.remove("apple")
thistuple3 = tuple(y)

# Remove Tuple
thistuple4 = ("apple", "banana", "cherry")
del thistuple4
#print(thistuple4) #ini akan menimbulkan kesalahan karena tuple sudah tidak ada lagi

## Unpack Tuple

# jumlah sama
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# jumlah beda / menggunakan bintang
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red) # dari cherry sampai raspberry, jadi list

## Loop Tuples
# For tanpa index
for x in thistuple:
  print(x)

# For dengan index
for i in range(len(thistuple)):
  print(thistuple[i])

# While loop
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

## Join Tuples
# Menambahkan
tuple1 = ("a","b")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# menggandakan
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)