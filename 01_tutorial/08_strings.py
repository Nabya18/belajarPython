# """
# String => diapit oleh tanda kutip tunggal atau tanda kutip ganda.
#     'halo' sama dengan "halo" .
#     a. String Multiline => menetapkan string multiline ke variabel dengan menggunakan tiga tanda kutip
#     b. string dalam Python adalah array byte yang mewakili karakter unicode.
#         Python tidak memiliki tipe data karakter, karakter tunggal hanyalah sebuah string dengan panjang 1.
#     c. Looping dalam string
#         Karena string adalah array, kita dapat melakukan perulangan karakter dalam string, dengan perulangan for.
#     d. Len => untuk mengetahui panjang karakter
#     e. Check String => Untuk memeriksa apakah ada frasa atau karakter tertentu dalam sebuah string
#         berisi True / False
#
# 1. Slicing Strings => mengembalikan serangkaian karakter
#     Tentukan indeks awal dan indeks akhir, dipisahkan dengan titik dua, untuk mengembalikan bagian dari string.
#     Karakter pertama memiliki indeks 0.
#     a. Slice From the Start
#         Dengan mengabaikan indeks awal, rentang akan dimulai dari karakter pertama
#     b. Slice To the End
#         mengabaikan indeks akhir , rentangnya akan menuju ke akhir
#     c. Negative Indexing
#         Gunakan indeks negatif untuk memulai potongan dari akhir string
#         Dibalik, dimulai dari akhir
#         Dimulai dari -1
#
# 2. Modify Strings
#     a. upper() => Huruf besar
#     b. lower() => Huruf kecil
#     c. strip() => menghilangkan spasi apa pun di awal dan atau akhir
#     d. replace() => menggantikan sebuah string dengan string lain
#     e. split() => membagi string menjadi substring jika menemukan contoh pemisah
#
# 3. Concatenate Strings => Untuk menggabungkan
#
# 4. Format Strings
#     a. tidak bisa menggabungkan string dan angka diakali dengan Format
#     b. mengambil argumen yang diteruskan, memformatnya, dan menempatkannya dalam string di mana placeholder {} berada
#
# 5. Escape Strings
#     a. Untuk menyisipkan karakter yang ilegal dalam sebuah string, gunakan karakter escape.
#     b. Karakter escape
#         # \'      Single Quote
#         # \\      Backslash
#         # \n      New Line
#         # \r      Carriage Return
#         # \t      Tab
#         # \b      Backspace
#         # \f      Form Feed
#         # \ooo    Octal value
#         # \xhh    Hex value
#
# 6. String Methods => Semua metode string mengembalikan nilai baru. Mereka tidak mengubah string aslinya.
#     Method	        Description
#     capitalize()	Converts the first character to upper case
#     casefold()	    Converts string into lower case
#     center()	    Returns a centered string
#     count()	        Returns the number of times a specified value occurs in a string
#     encode()	    Returns an encoded version of the string
#     endswith()	    Returns true if the string ends with the specified value
#     expandtabs()	Sets the tab size of the string
#     find()	        Searches the string for a specified value and returns the position of where it was found
#     format()	    Formats specified values in a string
#     format_map()	Formats specified values in a string
#     index()	        Searches the string for a specified value and returns the position of where it was found
#     isalnum()	    Returns True if all characters in the string are alphanumeric
#     isalpha()	    Returns True if all characters in the string are in the alphabet
#     isascii()	    Returns True if all characters in the string are ascii characters
#     isdecimal()	    Returns True if all characters in the string are decimals
#     isdigit()	    Returns True if all characters in the string are digits
#     isidentifier()	Returns True if the string is an identifier
#     islower()	    Returns True if all characters in the string are lower case
#     isnumeric()	    Returns True if all characters in the string are numeric
#     isprintable()	Returns True if all characters in the string are printable
#     isspace()	    Returns True if all characters in the string are whitespaces
#     istitle()	    Returns True if the string follows the rules of a title
#     isupper()	    Returns True if all characters in the string are upper case
#     join()	        Joins the elements of an iterable to the end of the string
#     ljust()	        Returns a left justified version of the string
#     lower()	        Converts a string into lower case
#     lstrip()	    Returns a left trim version of the string
#     maketrans()	    Returns a translation table to be used in translations
#     partition()	    Returns a tuple where the string is parted into three parts
#     replace()	    Returns a string where a specified value is replaced with a specified value
#     rfind()	        Searches the string for a specified value and returns the last position of where it was found
#     rindex()	    Searches the string for a specified value and returns the last position of where it was found
#     rjust()	        Returns a right justified version of the string
#     rpartition()	Returns a tuple where the string is parted into three parts
#     rsplit()	    Splits the string at the specified separator, and returns a list
#     rstrip()	    Returns a right trim version of the string
#     split()	        Splits the string at the specified separator, and returns a list
#     splitlines()	Splits the string at line breaks and returns a list
#     startswith()	Returns true if the string starts with the specified value
#     strip()	        Returns a trimmed version of the string
#     swapcase()	    Swaps cases, lower case becomes upper case and vice versa
#     title()	        Converts the first character of each word to upper case
#     translate()	    Returns a translated string
#     upper()	        Converts a string into upper case
#     zfill()	        Fills the string with a specified number of 0 values at the beginning
# """

## Contoh String Multiline
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Bukti string adalah array
a = "Hello, World!"
print(a[1])

# Contoh Looping dalam string
for x in "banana":
  print(x)

# Contoh Len
a = "Hello, World!"
print(len(a))

# Contoh check string (jika ada)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Contoh check string (tidak ada)
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is not present.")

## Contoh Slicing
b = "Hello, World!"
print(b[2:5])

print(b[:5]) # Contoh Slicing From the start
print(b[2:]) # Contoh Slice To the End
print(b[-5:-2]) # Contoh Negative Indexing

## Contoh modify
a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("l", "J"))
print(a.split(","))

## Contoh Concatenate
a = "Hello"
b = "World"
c = a + " " + b
print(c)

## Contoh Format String
quantity = 3
itemno = 567
price = 49.95
myorder1 = "I want {} pieces of item {} for {} dollars." # tanpa nomor index
myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}." # dengan nomor index
print(myorder1.format(quantity, itemno, price))
print(myorder2.format(quantity, itemno, price))

## Contoh escape string
txt = "We are the so-called \"Vikings\" from the north."
print(txt)