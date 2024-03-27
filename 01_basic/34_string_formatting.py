"""
Python String Formatting
    Untuk memastikan string akan ditampilkan seperti yang diharapkan, kita dapat memformat hasilnya dengan format() metode tersebut.

1. format string()
    a. format() => memungkinkan Kita memformat bagian string yang dipilih
    b. Terkadang ada bagian teks yang tidak Kita kendalikan, mungkin berasal dari database, atau input user
    c. Untuk mengontrol nilai tersebut, tambahkan placeholder (tKita kurung kurawal {}) pada teks, dan jalankan nilai melalui format() metode
    d. Kita dapat menambahkan parameter di dalam tKita kurung kurawal untuk menentukan cara mengonversi nilai

    Format String Python () Metode
    Definisi dan Penggunaan
        a. format() => memformat nilai yang ditentukan dan memasukkannya ke dalam placeholder string.
        b. Placeholder didefinisikan menggunakan tKita kurung kurawal
        c. format() => mengembalikan string yang diformat.

    Syntax
        string.format(value1, value2...)

    Placeholder
        Placeholder dapat diidentifikasi menggunakan indeks bernama {price}, indeks bernomor {0}, atau bahkan placeholder kosong {}

    Jenis Pemformatan
    :<		Left aligns the result (within the available space)
    :>		Right aligns the result (within the available space)
    :^		Center aligns the result (within the available space)
    :=		Places the sign to the left most position
    :+		Use a plus sign to indicate if the result is positive or negative
    :-		Use a minus sign for negative values only
    : 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
    :,		Use a comma as a thousand separator
    :_		Use a underscore as a thousand separator
    :b		Binary format
    :c		Converts the value into the corresponding unicode character
    :d		Decimal format
    :e		Scientific format, with a lower case e
    :E		Scientific format, with an upper case E
    :f		Fix point number format
    :F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
    :g		General format
    :G		General format (using a upper case E for scientific notations)
    :o		Octal format
    :x		Hex format, lower case
    :X		Hex format, upper case
    :n		Number format
    :%		Percentage format

2. Multiple Values
    a. Jika Kita ingin menggunakan lebih banyak nilai, cukup tambahkan lebih banyak nilai ke metode format()
    b. Dan tambahkan lebih banyak placeholder

3. Index Numbers
    Kita dapat menggunakan nomor indeks (angka di dalam tKita kurung kurawal {0}) untuk memastikan nilai ditempatkan pada placeholder yang benar

4. Named Indexes
    a. Kita juga dapat menggunakan indeks bernama dengan memasukkan nama di dalam tKita kurung kurawal {carname}
    b. namun Kita harus menggunakan nama ketika meneruskan nilai parameter txt.format(carname = "Ford")
"""
## 1. Format string()
# Tambahkan placeholder tempat Kita ingin menampilkan harga
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Format harga yang akan ditampilkan sebagai angka dengan dua desimal
txt = "The price is {:.2f} dollars"

# contoh Menggunakan nilai placeholder yang berbeda
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

# contoh jenis pemformatan
# 1. Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(5))

# 2. Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))


## 2. Multiple values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

## 3. Index number
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# jika Kita ingin merujuk ke nilai yang sama lebih dari sekali, gunakan nomor indeks
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

## 4. Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))