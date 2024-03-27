"""
Python Try Except
    1. try => memungkinkan Kita menguji blok kode untuk menemukan kesalahan.
    2. except => memungkinkan Kita menangani kesalahan tersebut.
    3. else => memungkinkan Kita mengeksekusi kode ketika tidak ada kesalahan.
    4. finally => memungkinkan Kita mengeksekusi kode, terlepas dari hasil blok coba dan kecuali.

1. Exception Handling
    a. Ketika kesalahan terjadi, atau pengecualian seperti yang kita sebut, Python biasanya akan berhenti dan menghasilkan pesan kesalahan.
    b. Pengecualian ini dapat ditangani dengan menggunakan try pernyataan
    c. Jika blok try menimbulkan kesalahan, blok except akan dieksekusi.
    d. Tanpa blok try, program akan crash dan menimbulkan kesalahan

2. Many Exceptions
    Kita dapat menentukan blok pengecualian sebanyak yang Kita inginkan, misalnya jika Kita ingin mengeksekusi blok kode khusus untuk jenis kesalahan khusus

3. Else
    Kita dapat menggunakan elsekata kunci untuk menentukan blok kode yang akan dieksekusi jika tidak ada kesalahan yang muncul

4. finally
    a. Blok finally, jika ditentukan, akan dieksekusi terlepas dari apakah blok percobaan menimbulkan kesalahan atau tidak.
    b. Ini berguna untuk menutup objek dan membersihkan sumber daya
    c. Program dapat dilanjutkan tanpa membiarkan objek file terbuka.

5. Raise an exception
    a. Sebagai pengembang Python, Kita dapat memilih untuk memberikan pengecualian jika suatu kondisi terjadi.
    b. Untuk memunculkan (atau menaikkan) pengecualian, gunakan raisekata kunci.
    c. Kata raisekunci digunakan untuk memunculkan pengecualian.
    d. Kita dapat menentukan jenis kesalahan yang akan dimunculkan, dan teks yang akan dicetak kepada pengguna.

"""

# 1. Exception Handling
#The try block will generate an error, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")

# 2. Many Exceptions
#The try block will generate a NameError, because x is not defined
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# 3. Else
#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# 4. Finally
#The finally block gets executed no matter if the try block raises any errors or not:

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# membuka dan menulis ke file yang tidak dapat ditulisi
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# 5. Raise an exception
# Munculkan kesalahan dan hentikan program jika x lebih rendah dari 0
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# Naikkan TypeError jika x bukan bilangan bulat
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")