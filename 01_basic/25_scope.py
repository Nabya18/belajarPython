"""
Python Scope: Variabel hanya tersedia dari dalam wilayah pembuatannya
1. Local Scope
    a. Variabel yang dibuat di dalam suatu fungsi termasuk dalam lingkup lokal fungsi tersebut, dan hanya dapat digunakan di dalam fungsi tersebut.
    b. Fungsi Di Dalam Fungsi: variabel local tidak tersedia di luar fungsi, namun Variabel lokal dapat diakses dari suatu fungsi di dalam fungsi tersebut
2. Global Scope
    a. Variabel yang dibuat di bagian utama kode Python adalah variabel global dan termasuk dalam cakupan global.
    b. Variabel global tersedia dalam lingkup apa pun, global dan lokal.
    c. Penamaan Variabel
        - Dalam Python, jika nama variabel yang sama digunakan di dalam dan di luar fungsi, itu dianggap sebagai dua variabel terpisah
        - satu dalam lingkup global dan satu dalam lingkup lokal.
3. Global Keyword
    a. Jika Kita perlu membuat variabel global, tetapi terjebak dalam lingkup lokal, Kita dapat menggunakan globalkata kunci.
    b. Kata global kunci membuat variabel menjadi global.
    c. gunakan global kata kunci jika Kita ingin membuat perubahan pada variabel global di dalam suatu fungsi.
"""
## 1. Local Scope
# Variabel yang dibuat di dalam suatu fungsi tersedia di dalam fungsi itu
def myfunc():
  x = 300
  print(x)

myfunc()

# Fungsi Di Dalam Fungsi
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

## 2. Lingkup Global
# Variabel yang dibuat di luar suatu fungsi bersifat global dan dapat digunakan oleh siapa saja
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# dua variabel terpisah => Fungsi tersebut akan mencetak local x, dan kemudian kode akan mencetak global x
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

## 3. Kata Kunci Global
# Jika Kita menggunakan global kata kunci, variabel tersebut termasuk dalam cakupan global
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Untuk mengubah nilai variabel global di dalam suatu fungsi, rujuk variabel tersebut dengan menggunakan global kata kunci
x = 300

def myfunc():
  global x  #engubah nilai variabel global di dalam suatu fungsi
  x = 200

myfunc()

print(x)