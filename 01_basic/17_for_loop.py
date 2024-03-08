"""
Perulangan for => digunakan untuk mengulangi suatu urutan (baik berupa list, tupel, dict, set, atau string).
Note: Perulangan for tidak memerlukan variabel pengindeksan untuk disetel sebelumnya.
    1. break => menghentikan perulangan sebelum perulangan tersebut melewati semua item
    2. continue => menghentikan iterasi perulangan saat ini, dan melanjutkan dengan perulangan berikutnya
    3. range => mengulang sekumpulan kode beberapa kali tertentu, dimulai dari 0 secara default.
    4. else => menentukan blok kode yang akan dieksekusi ketika perulangan selesai

Blok else TIDAK akan dieksekusi jika perulangan dihentikan oleh sebuah breakpernyataan.

Loop nested => Loop dalam loop menggunakan for
1. "Loop dalam" akan dieksekusi satu kali untuk setiap iterasi dari "loop luar"
2. for loop statement tidak boleh kosong, gunakan pass jika diperlukan

Untuk range bisa dilihat di 08_strings.py bagian slicing
"""

## contoh
# Cetak setiap buah dalam daftar buah
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # di print secara vertical

# perulangan melalui string / huruf demi huruf
for x in "banana":
  print(x)

# contoh break 1: selesai perulangan ketika x = "pisang"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# contoh break 2: selesai perulangan sebelum ketika x = "pisang"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# contoh continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":  #banana di skip
    continue
  print(x)

# contoh range
for x in range(6): # tanpa parameter awal
  print(x)

for x in range(2, 6): # dengan parameter awal
  print(x)

# range seperti deret aritmetika
for x in range(2, 30, 3):
  print(x)

# contoh else dieksekusi
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# contoh else tidak di eksekusi karena ada break
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# contoh loop nested
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
country = ["indonesia", "china", "Jepang"]
# row[adj] = fruits * country

for x in adj:
  for y in fruits:
    for z in country:
        print(x, y, z)

# contoh pass
for x in [0, 1, 2]:
  pass

# contoh lain
for x in adj:
    print(x)
    for y in fruits:
        print("-", y)
        for z in country:
            print("*", z)