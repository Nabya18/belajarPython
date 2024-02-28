"""
Boolean => True or False

1.  Nilai Boolean => hasilnya True atau False
2.  Evaluasi Nilai dan Variabel
    bool() => mengevaluasi nilai apa pun dan memberi hasil True atau False
    - String apa pun adalah True, kecuali string kosong.
    - Number apa pun adalah True, kecuali 0.
    - List, tuple, set, dan dict apapun True, kecuali kosong
    - False bernilai False
    - False jika objek yang dibuat dari kelas dengan __len__fungsi yang mengembalikan 0atau False
3. Fungsi dapat mengembalikan Boolean

Python juga memiliki banyak fungsi bawaan yang mengembalikan nilai boolean.
Contoh, isinstance() => dapat digunakan untuk menentukan apakah suatu objek bertipe data tertentu sesuai
"""

## Mengembalikan jawaban boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

## Contoh Evaluasi Nilai dan Variabel
x = "" # False
y = " " # True
z = 15

print(bool(x))
print(bool(y))
print(bool(z))

## Contoh kelas __len__
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

## Fungsi mengembalikan boolean
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

## Contoh isinstance
x = 200
print(isinstance(x, int))