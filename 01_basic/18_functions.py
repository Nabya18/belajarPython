"""
Fungsi adalah blok kode yang hanya berjalan ketika dipanggil.
1. Kita dapat meneruskan data, yang dikenal sebagai parameter, ke dalam suatu fungsi.
2. Suatu fungsi dapat mengembalikan data sebagai hasilnya.

Argumen => sering kali disingkat menjadi args dalam dokumentasi Python.
1. Informasi dapat diteruskan ke fungsi sebagai argumen.
2. Argumen ditentukan setelah nama fungsi, di dalam tanda kurung.
3. Kita dapat menambahkan argumen sebanyak yang diinginkan, cukup pisahkan dengan koma.


parameter dan argumen dapat digunakan untuk hal yang sama: informasi yang diteruskan ke suatu fungsi.
Dari perspektif fungsi:
1. Parameter adalah variabel yang tercantum di dalam tanda kurung pada definisi fungsi.
2. Argumen adalah nilai yang dikirim ke fungsi saat dipanggil.

Catatan: Argumen sering kali disingkat menjadi args dalam dokumentasi Python.

Jumlah argumen:
1. Secara default, suatu fungsi harus dipanggil dengan jumlah argumen yang benar.
2. jika fungsi mengharapkan 2 argumen, kita harus memanggil fungsi tersebut dengan 2 argumen, tidak lebih, dan tidak kurang.


Argumen Arbitrary / sewenang-wenang, *args:
1. Jika kita tidak tahu berapa banyak argumen yang akan diteruskan ke fungsi, tambahkan *sebelum nama parameter dalam definisi fungsi.
2. Dengan cara ini fungsi akan menerima tuple of arguments, dan dapat mengakses item yang sesuai

Argumen Sewenang-wenang sering disingkat menjadi *args dalam dokumentasi Python.


Argumen keywords:
1. Kita dapat mengirim argumen dengan sintaks key = value
2. Dengan cara ini urutan argumen tidak menjadi masalah.

Ungkapan Argumen Keywords sering disingkat menjadi kwargs dalam dokumentasi Python.


Argumen keywords arbitrary, **kwargs:
1. Jika idak tahu berapa banyak argumen keyword yang akan dimasukkan ke dalam fungsi, tambahkan **sebelum nama parameter dalam definisi fungsi.
2. Dengan cara ini fungsi akan menerima dict argumen, dan dapat mengakses item yang sesuai

Argumen Kword Sewenang-wenang sering disingkat menjadi **kwargs dalam dokumentasi Python.


Default Parameter Value:
Jika kita memanggil fungsi tanpa argumen, maka fungsi tersebut akan menggunakan nilai default


Passing a List as an Argument:
1. dapat mengirim tipe data argumen apa pun ke suatu fungsi  (string, number, list, dictionary etc.)
2. itu akan diperlakukan sebagai tipe data yang sama di dalam fungsi.

jika Anda mengirimkan list sebagai argumen, itu akan tetap menjadi list ketika mencapai fungsi


Return value:
Untuk membiarkan suatu fungsi mengembalikan nilai, gunakan return


The pass Statement:
function definisi tidak boleh kosong, tetapi jika karena alasan tertentu kita memiliki functiondefinisi tanpa konten, masukkan passpernyataan untuk menghindari kesalahan.


Positional-Only Arguments:
1. Kita dapat menentukan bahwa suatu fungsi HANYA dapat memiliki argumen posisi, atau HANYA argumen keyword.
2. Untuk menentukan bahwa suatu fungsi hanya dapat memiliki argumen posisi, tambahkan , / setelah argumen


Argumen keywords only:
Untuk menentukan bahwa suatu fungsi hanya dapat memiliki argumen keyword, tambahkan *, sebelum argumen


Kombinasi positional-only dan keyword-only:
1. Kita bisa menggabungkan dua tipe argumen dalam fungsi yang sama.
2. Argumen apa pun sebelum / ,hanya bersifat posisitional, dan argumen apa pun setelahnya*, hanya bersifat keyword.


Rekursif:
1. Python juga menerima rekursi fungsi, yang berarti fungsi yang ditentukan dapat memanggil dirinya sendiri.
2. Rekursi adalah konsep matematika dan pemrograman yang umum. Artinya suatu fungsi memanggil dirinya sendiri.
3. Manfaat rekursif => kita dapat mengulang data untuk mencapai hasil.

Note rekursif:
1. Kita harus sangat berhati-hati dengan rekursi karena sangat mudah untuk menulis fungsi yang tidak pernah berhenti, atau fungsi yang menggunakan memori atau daya prosesor dalam jumlah berlebih.
2. Rekursif perlu ditulis dengan benar agar efisien dan elegan secara matematis.

tri_recursion() => adalah fungsi yang telah kita definisikan untuk memanggil dirinya sendiri ("recurse")
penjelasan hasil: Ini karena pada setiap tingkat rekursi, kita menambahkan nilai k saat ini dengan nilai yang dikembalikan dari rekursi sebelumnya, dan kemudian mencetak hasilnya.


Poin penting tentang rekursi:
1. Kondisi Dasar (Base Case): Kondisi dasar adalah situasi di mana fungsi berhenti memanggil dirinya sendiri dan mengembalikan nilai langsung tanpa rekursi tambahan.
2. Pemecahan Masalah Berulang: Konsep utama di balik rekursi adalah pemecahan masalah berulang.
3. Kemungkinan Terjadi Penumpukan Tumpukan (Stack Overflow): Hal ini terjadi ketika terlalu banyak panggilan rekursif bertumpuk di dalam tumpukan memori yang terbatas. Ini bisa menyebabkan program menjadi tidak responsif atau mengalami kegagalan.
4. Kompleksitas dan Efisiensi: Rekursi bisa menjadi alat yang sangat kuat untuk menyelesaikan beberapa masalah dengan kode yang bersih dan mudah dipahami.
5. Pemahaman dan Pemeliharaan Kode: Kode yang menggunakan rekursi mungkin memerlukan pemahaman yang lebih dalam terhadap masalah yang dipecahkan dan cara kerja rekursi itu sendiri.
"""


# contoh
def my_function():
    print("Hello from a function")

my_function() # memanggil fungsi

# contoh argumen
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# contoh fungsi mengharapkan 2 argumen
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")


# argumen *args, Jika jumlah argumen tidak diketahui
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# argumen keywords
def my_function(child3, child2, child1):
    print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# argumen keyword arbitrary, **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# contoh default parameter
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function() #tanpa argumen
my_function("Brazil")


# contoh passing a list
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# contoh return value
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# definisi function kosong
def myfunction():
    pass


# contoh Positional-Only
def my_function(x, /):
    print(x)

my_function(3)


# contoh argumen keyword only
def my_function(*, x):
    print(x)

my_function(x = 3)


# Kombinasi positional-only dan keyword-only
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


# contoh rekursif
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6) # dari 1, 2, 3, 4, 5, 6