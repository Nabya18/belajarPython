"""
List => digunakan untuk menyimpan banyak item dalam satu variabel
    a. Access List Items => dapat mengaksesnya dengan mengacu pada nomor indeks
       Range of index = menentukan rentang indeks dengan menentukan di mana memulai dan di mana mengakhiri
    b. Change List Items => mengubah menggunakan index
        Jika memasukkan lebih banyak / lebih sedikit item daripada yang digantikan, item baru akan dimasukkan ke tempat yang telah dtentukan, dan item lainnya akan dipindahkan sesuai
    c. Add List Items
        - Append => Untuk menambahkan item ke akhir list
        - Insert => Untuk menyisipkan item list pada indeks tertentu, tanpa mengganti nilai apa pun yang sudah ada
        - Extend => Untuk menambahkan elemen dari list lain ke list saat ini
    d. Remove List Items
        - Remove Specified Item => remove()
          Jika terdapat lebih dari satu item dengan nilai yang ditentukan, remove()metode ini akan menghilangkan kemunculan pertama
        - Remove Specified Index
          - pop() => menghapus indeks yang ditentukan, Jika tidak menentukan indeks, pop()metode ini akan menghapus item terakhir.
          - del => menghapus indeks yang ditentukan dan dapat menghapus list sepenuhnya
        - Clear the List => clear(), listnya masih ada, tetapi tidak ada isinya
    e. Loop Lists
    f. List Comprehension
    g. Sort Lists
    h. Copy Lists
    i. Join Lists
    j. List Methods

Karakteristik List:
    1. diurutkan => memiliki urutan yang ditentukan, dan urutan itu tidak akan berubah.
    2. dapat diubah => dapat mengubah, menambah, dan menghapus item dalam daftar setelah dibuat.
    3. memungkinkan nilai duplikat => daftar dapat memiliki item dengan nilai yang sama
    4. diindeks, item pertama memiliki indeks [0], item kedua memiliki indeks, [1]dll.
    5. item dapat berupa tipe data apa pun
    6. dapat menggunakan list() constructor

len() => menentukan berapa banyak item yang dimiliki suatu daftar

Tipe data collection dalam bahasa pemrograman Python:
    a. Daftar => kumpulan yang terurut dan dapat diubah. Mengizinkan anggota duplikat.
    b. Tuple => koleksi yang tertata dan tidak dapat diubah. Mengizinkan anggota duplikat.
    c. Set => koleksi yang tidak berurutan, tidak dapat diubah*, dan tidak terindeks. Tidak ada anggota duplikat.
    d. Dict => kumpulan yang diurutkan** dan dapat diubah. Tidak ada anggota duplikat.


"""

## Contoh Item lists
list1 = ["apple", "banana", "cherry"] #string
list2 = [1, 5, 7, 9, 3] #int
list3 = [True, False, False] #boolean
list4 = list1 = ["abc", 34, True, 40, "male"] #campuran

# contoh len dalam list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(len(thislist))
print(type(thislist))

# contoh list() constructor
myList = list(("apple", "banana", "cherry")) # note the double round-brackets
print(myList)

## Contoh Access Lists
print(thislist[1])
print(thislist[-1]) #Pengindeksan negatif berarti memulai dari akhir
print(thislist[2:5]) #rentang index dimulai pada indeks 2 dan berakhir pada indeks 4.
print(thislist[:4]) #rentang akan dimulai dari item pertama sampai index ke 3
print(thislist[2:]) #rentang dimulai dari index 2 sampai akhir
print(thislist[-4:-1]) #tidak sampai index terakhir

# Check apakah item ada menggunakan if
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

## Contoh Change List
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

myList[1:2] = ["blackcurrant", "watermelon"]
print(myList)

myList[1:3] = ["watermelon"]
print(myList)

## Contoh Add
# Append
thislist.append("Blueberry")
print(thislist)

# Contoh insert
myList.insert(2, "strawberry")
print(myList)

# Contoh extend
thislist.extend(myList)
print(thislist)

"""
extend() tidak harus menambahkan list , kita dapat menambahkan objek apa pun yang dapat diubah (tupel, set, dict, dll.).
"""
isList = ["apple", "banana", "cherry"]
isTuple = ("kiwi", "orange")
isList.extend(isTuple)
print(isList) #jadi list

## Contoh Remove Lists
# Remove Specified Item
thislist1 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist1.remove("banana")
print(thislist1)

# Remove Specified Index pop()
thislist2 = ["apple", "banana", "cherry"]
thislist2.pop(1)
print(thislist2)
thislist2.pop() #menghapus item terakhir
print(thislist2)

# Remove Specified Index del
thislist3 = ["apple", "banana", "cherry"]
del thislist3[0]
print(thislist3)
del thislist3 #menghapus list sepenuhnya

# Remove Specified Index clear()
thislist4 = ["apple", "banana", "cherry"]
thislist4.clear()
print(thislist4)