"""
Python mengandalkan indentasi (spasi di awal baris) untuk menentukan cakupan dalam kode.
Python mendukung kondisi logis yang biasa dari matematika:
    - Sama dengan: a == b
    - Tidak Sama dengan: a != b
    - Kurang dari: a < b
    - Kurang dari atau sama dengan: a <= b
    - Lebih besar dari: a > b
    - Lebih besar dari atau sama dengan: a >= b

Macam-macam kondisi:
a. if
b. elif => jika kondisi sebelumnya tidak benar, maka coba kondisi ini
c. else => menangkap apa pun yang tidak tertangkap oleh kondisi sebelumnya

Kondisi ini dapat digunakan dalam beberapa cara, paling umum dalam "pernyataan if" dan perulangan.
Sebuah "pernyataan if" ditulis dengan menggunakan kata kunci if .

if nested => if dalam if

if pernyataan tidak boleh kosong,
pass => jka pernyataan if kosong
"""

# contoh if
a = 33
b = 200
if b > a:
  print("b is greater than a")

# contoh elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# contoh else > Jika hanya mempunyai satu pernyataan untuk dieksekusi
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

## Format lain penulisan if statement
# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else => Jika hanya mempunyai satu pernyataan untuk dieksekusi, satu untuk if, dan satu lagi untuk else
print("A") if a > b else print("B")

print("A") if a > b else print("=") if a == b else print("B")

# And
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Or
if a > b or a > c:
  print("At least one of the conditions is True")

# not
if not a > c:
  print("a is NOT greater than c")

# if nested
x = 19

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# contoh pernyataan if kosong
if b > a:
  pass