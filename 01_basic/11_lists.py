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
    e. Loop Lists => pengulangan dalam list
        - for loop
        - While Loop
    f. List Comprehension => menawarkan sintaks yang lebih pendek
        - newlist = [expression for item in iterable]
        - Memanipulasi hasil dengan expression
    g. Sort Lists => default ascending
        - reverse = True => Untuk mengurutkan secara descending
        - semua huruf kapital diurutkan sebelum huruf kecil
        - key = str.lower => agar tidak case sensitive
        - reverse() => membalik urutan pengurutan elemen saat ini.
    h. Copy Lists
        tidak dapat copy list hanya dengan mengetik list2 = list1
        karena list2hanya akan menjadi referensi ke list1
        perubahan yang dilakukan list1secara otomatis juga akan dilakukan di list2
        - copy() => untuk membuat salinan
        - list()
    i. Join Lists => menggabungkan list
        - by using the + operator
        - by appending all the items from list2 into list1
        - extend() => menambahkan elemen dari satu daftar ke daftar lainnya
    j. List Methods
        Method	            Description
        append()	        Menambahkan elemen di akhir list
        clear()	            Menghapus semua elemen dari list
        copy()	            Mengembalikan salinan list
        count()	            Mengembalikan jumlah elemen dengan nilai yang ditentukan
        extend()	        Menambahkan elemen list (atau apa pun yang dapat diubah), ke akhir list saat ini
        index()	            Mengembalikan indeks elemen pertama dengan nilai yang ditentukan
        insert()	        Menambahkan elemen pada posisi yang ditentukan
        pop()	            Menghapus elemen pada posisi yang ditentukan
        remove()	        Menghapus item dengan nilai yang ditentukan
        reverse()	        Membalikkan urutan list
        sort()	            Mengurutkan list

Karakteristik List:
    1. ditulis dengan []
    2. diurutkan => memiliki urutan yang ditentukan, dan urutan itu tidak akan berubah.
    3. dapat diubah => dapat mengubah, menambah, dan menghapus item dalam daftar setelah dibuat.
    4. memungkinkan nilai duplikat => daftar dapat memiliki item dengan nilai yang sama
    5. diindeks, item pertama memiliki indeks [0], item kedua memiliki indeks, [1]dll.
    6. item dapat berupa tipe data apa pun
    7. dapat menggunakan list() constructor

len() => menentukan berapa banyak item yang dimiliki suatu daftar

Tipe data collection dalam bahasa pemrograman Python:
    a. List => kumpulan yang terurut dan dapat diubah. Mengizinkan anggota duplikat.
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

## Loop list
# For Loop
for x in thislist:
  print(x) #value of list

thislist5 = ["apple", "banana", "cherry"]
for i in range(len(thislist5)):
  print(thislist5[i]) #mengacu pada nomor indeksnya

# While Loop => mengacu pada indeks
i = 0
while i < len(thislist):
  print("ini while loop",thislist[i])
  i = i + 1

# menggunakan comprehensive list
[print("ini comprehensive list",x) for x in thislist]

## List Comprehensive
# tanpa List Comprehensive
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print("Tanpa Comprehensive",newlist)

# Dengan List Comprehensive
newlist = [x for x in fruits if "a" in x] # dengan kondisi
newlist1 = [x for x in range(10)] # dengan range
newlist2 = [x for x in range(10) if x < 5] # dengan range dan kondisi
print("Dengan Comprehensive",newlist)

# Memanipulasi hasil dengan expresi
newlist3 = [x.upper() for x in fruits] # menjadi huruf kapital
newlist4 = ['hello' for x in fruits] # merubah semua nilai menjadi hello
newlist5 = [x if x != "banana" else "orange" for x in fruits] # "Return the item if it is not banana, if it is banana return orange".

## Sort List
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

#dengan fungsi
def myfunc(n):
  return abs(n - 50)

thisnumlist = [100, 50, 65, 82, 23]
thisnumlist.sort(key = myfunc)
print(thisnumlist)

# agar tidak case sensitive
thislist.sort(key = str.lower)
print(thislist)

# membalik urutan list
thislist5.reverse()
print(thislist5)

## Copy List
# Copy
thiscopylist = thislist.copy()
print(thiscopylist)

#list
thislistlist = list(thislist)
print(thislistlist)

## Join List
# dengan operator +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# dengan append
for x in list2:
  list1.append(x)

print(list1)

# dengan extend
list1.extend(list2)
print(list1)