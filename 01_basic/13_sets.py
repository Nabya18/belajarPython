"""
Set digunakan untuk menyimpan banyak item dalam satu variabel.
1. Access Set => tidak dapat mengakses item dalam satu set dengan mengacu pada indeks atau kunci.
    - for => mengulang kumpulan item
    - in => menanyakan apakah ada nilai tertentu dalam kumpulan
2. Add Set Items
    - add() => Untuk menambahkan satu item ke set
    - update() => Untuk menambahkan item dari kumpulan lain ke kumpulan saat ini
      Objek dalam update()metode tidak harus berupa himpunan, dapat berupa objek apa pun yang dapat diubah (tupel, list, dict, dll.).
3. Remove Set
    - remove() => Untuk menghapus nilai yang dicari. Jika nilai yang dicari tidak ada, maka akan error.
    - discard() => Untuk menghapus nilai yang dicari. Jika nilai yang dicari tidak ada, tidak akan error.
    - pop() => Hapus item acak / Mengambil dan menghapus nilai yang ada di sebelah kiri.
        metode ini akan menghapus item secara acak, sehingga kita tidak dapat memastikan item apa yang dihapus.
    - clear() => mengosongkan set
    - del => menghapus set sepenuhnya
4. Loop Set => pengulangan menggunakan for loop
5. Join Set
   union()dan update() akan mengecualikan item duplikat apa pun.
    - union() => Gabungan / metode yang mengembalikan kumpulan baru yang berisi semua item dari kedua kumpulan
    - update() => menyisipkan semua item dari satu kumpulan ke kumpulan lainnya
    - intersection_update() => hanya akan menyimpan item yang ada di kedua set.
    - intersection() => Irisan / akan mengembalikan kumpulan baru , yang hanya berisi item yang ada di kedua kumpulan.
    - difference() => proses mengekstrak anggota grup pertama, yang bukan anggota grup kedua.
    - symmetric_difference_update() => hanya akan menyimpan elemen yang TIDAK ada di kedua set.
    - symmetric_difference() => akan mengembalikan anggota-anggota dari kedua grup, yang mana tiap anggota tersebut hanya menjadi anggota dari satu grup saja
      Nilai True and 1dianggap sebagai nilai yang sama dalam kumpulan, dan diperlakukan sebagai duplikat
6. Set Methods
    Method	                            Description
    add()	                            Adds an element to the set
    clear()	                            Removes all the elements from the set
    copy()	                            Returns a copy of the set
    difference()	                    Returns a set containing the difference between two or more sets
    difference_update()	                Removes the items in this set that are also included in another, specified set
    discard()	                        Remove the specified item
    intersection()	                    Returns a set, that is the intersection of two other sets
    intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
    isdisjoint()	                    Returns whether two sets have a intersection or not
    issubset()	                        Returns whether another set contains this set or not
    issuperset()	                    Returns whether this set contains another set or not
    pop()	                            Removes an element from the set
    remove()	                        Removes the specified element
    symmetric_difference()	            Returns a set with the symmetric differences of two sets
    symmetric_difference_update()	    inserts the symmetric differences from this set and another
    union()	                            Return a set containing the union of sets
    update()	                        Update the set with the union of this set and others

Karakteristik set:
1. tidak berurutan: item akan muncul dalam urutan acak.
2. tidak dapat diubah*: tidak dapat mengubah item setelah set dibuat, tetapi dapat menambahkan item baru.
3. tidak mengizinkan nilai duplikat: Set tidak boleh memiliki dua item dengan nilai yang sama.
4. Himpunan ditulis dengan kurung kurawal {}
5. Item kumpulan dapat muncul dalam urutan berbeda setiap kali kita menggunakannya, dan tidak dapat dirujuk berdasarkan indeks atau kunci.
6. True dan 1 dianggap nilai yang sama, dan dianggap duplikat
7. False and 0 dianggap nilai yang sama, dan dianggap duplikat
8. len() => Untuk menentukan berapa banyak item yang dimiliki suatu set
9. item dapat berupa tipe data apa pun
10. dapat menggunakan tuple() constructor
11. immutable
"""

## Contoh Set
thisset = {"apple", "banana", "cherry", "apple", True, 1, 2}
print(thisset)

# set konstruktor
thisset1 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset1)

## Contoh Access Set
# for
for x in thisset:
  print(x)

# in
print("banana" in thisset)

## Add set
# add()
thisset.add("orange")
print(thisset)

# update ()
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

# update() dengan berbagai object
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

## Remove set
# remove()
thisset2 = {"apple", "banana", "cherry"}

thisset2.remove("banana")
print(thisset2)

# discard()
thisset3 = {"apple", "banana", "cherry"}

thisset3.discard("banana")
print(thisset3)

# pop()
x = thisset2.pop()

print(x)
print(thisset2)

# clear()
thisset2.clear()
print(thisset2)

# del
del thisset3
#print(thisset3) #undefined karena sudah dihapus

## Join Set
# union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# intersection_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# symmetric_difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# symmetric_difference()
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)