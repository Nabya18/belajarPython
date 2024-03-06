"""
dictionary: digunakan untuk menyimpan nilai data dalam pasangan key:value.
Karakteristik dictionary:
    1. kumpulan yang terurut*: item-item tersebut memiliki urutan yang ditentukan, dan urutan itu tidak akan berubah.
    2. dapat diubah: dapat mengubah, menambah atau menghapus item setelah kamus dibuat.
    3. tidak mengizinkan duplikat: tidak boleh memiliki dua item dengan kunci yang sama.
    4. ditulis dengan tanda kurung kurawal, dan memiliki kunci serta nilai
    5. dapat dirujuk dengan menggunakan nama kunci.
    6. tidak dapat merujuk ke suatu item dengan menggunakan indeks.
    7. len() => Untuk menentukan berapa banyak item yang dimiliki kamus
    8. Nilai dalam item dict dapat berupa tipe data apa pun
    9. dapat menggunakan konstruktor dict() untuk membuat dict

1. Access => mengakses item dict dengan mengacu pada nama kuncinya
    - get()
    - keys() => mengembalikan semua key dalam kamus.
    - value() => mengembalikan semua value dalam kamus.
    - items() => mengembalikan semua key:value dalam kamus
    - in => Untuk menentukan apakah kunci tertentu ada dalam kamus
2. Change
    - change value => mengubah nilai item tertentu dengan mengacu pada nama kuncinya
    - update dict => memperbarui kamus dengan item dari argumen yang diberikan.
        Argumennya harus berupa kamus, atau objek yang dapat diubah dengan pasangan kunci:nilai.
3. Add
    - Adding items => menggunakan kunci indeks baru dan memberikan nilai padanya
    - update() => akan memperbarui kamus dengan item dari argumen tertentu. Jika item tidak ada maka item akan ditambahkan.
4. Remove
    - pop() => menghapus item dengan nama kunci yang ditentukan
    - popitem() => menghapus item yang terakhir dimasukkan (di versi sebelum 3.7, item acak malah dihapus)
    - del => enghapus item dengan nama kunci yang ditentukan / menghapus dict sepenuhnya
    - clear() => mengosongkan dict
5. Loop => mengulang dict
    - values() => mengulang nilai
    - keys() => mengulang kunci
    - items() => mengulang nilai dan kunci
6. Copy
    sama halnya dengan lists, dict tidak dapat menyalin dengan dict2 = dict1
    hal itu dapat menjadi referensi ke dict1, perubahan di dict1 otomatis ke dict2
    - copy()
    - dict()
7. Nested => dict berisi dict atau disebut dict bersarang
    Untuk mengakses item dari kamus bertumpuk, Kita menggunakan nama kamus, dimulai dengan kamus luar
8. Dictionary Methods
    Method	            Description
    clear()	            Menghapus semua elemen dari dictionary
    copy()	            Returns salinan dictionary
    fromkeys()	        Returns kamus dengan kunci dan nilai yang ditentukan
    get()	            Returns nilai kunci yang ditentukan
    items()	            Returns list yang berisi tupel untuk setiap pasangan nilai kunci
    keys()	            Returns a list yang berisi kunci dict
    pop()	M           enghapus elemen dengan kunci yang ditentukan
    popitem()	        Menghapus pasangan nilai kunci yang terakhir dimasukkan
    setdefault()	    Returns nilai kunci yang ditentukan. Jika kunci tidak ada: masukkan kunci dengan nilai yang ditentukan
    update()	        Memperbarui kamus dengan pasangan nilai kunci yang ditentukan
    values()	        Returns a list semua nilai dalam dictionary
"""

## contoh dict
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))

# membuat dict() menggunakan konstruktor dict()
thisdict1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict1)

## Access
# - get()
x = thisdict.get("brand")
print(x)

# - keys()
x = thisdict.keys()
print(x)

# merubah dict dengan key
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

# - value()
x = thisdict.values()
print(x)

# merubah dict dengan value
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
car["color"] = "red"
print(x) #after the change

# - items()
x = thisdict.items()
print(x)

# merubah dict dengan items
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

# - in
if "brand" in thisdict:
  print("Yes, 'brand' is one of the keys in the thisdict dictionary")

## contoh change
# change value
car["year"] = 2018
print(car)

# update()
car.update({"year": 2020})
print(car)

## Adding
car["price"] = 150000000
print(car)

# update()
car.update({"price": 1500000000})
print(car)

## Remove
# pop()
car.pop("model")
print(car)

# popitem()
car.popitem()
print(car)

# del menghapus item
#del car["model"]
#print(car)

# del menghapus dict sepenuhnya
#del thisdict1
#print(thisdict1) #this will cause an error because "thisdict" no longer exists.

# clear()
car.clear()
print(car)

## Perulangan

# 1. Cetak semua nama kunci dalam list, satu per satu
for x in thisdict:
  print(x)

# 2. Cetak semua nama kunci dalam list, satu per satu menggunakan keys()
for x in thisdict.keys():
  print(x)

# 1. Cetak semua nilai dalam dict, satu per satu
for x in thisdict:
  print(thisdict[x])

# 2. Cetak semua nilai dalam dict, satu per satu dengan value()
for x in thisdict.values():
  print(x)

# Ulangi key dan value , dengan menggunakan items() metode
for x, y in thisdict.items():
  print(x,":", y)

## Copy
# copy()
mydict = thisdict.copy()
print(mydict)

# dict()
mydict = dict(thisdict)
print(mydict)

## dict nested
# menambahkan tiga kamus ke dalam kamus baru
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# akses dict nested
print(myfamily["child2"]["name"])