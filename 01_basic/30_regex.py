"""
Python RegEx
    1. RegEx, atau Regular Expression, adalah rangkaian karakter yang membentuk pola pencarian.
    2. RegEx dapat digunakan untuk memeriksa apakah suatu string berisi pola pencarian yang ditentukan.

1. Modul RegEx
    Python memiliki paket bawaan bernama re => yang dapat digunakan untuk bekerja dengan Ekspresi Reguler.
2. RegEx dengan Python
    Ketika Kita telah mengimpor remodul, Kita dapat mulai menggunakan ekspresi reguler
3. Fungsi RegEx
    Function	    Description
    findall	        Returns a list containing all matches
    search	        Returns a Match object if there is a match anywhere in the string
    split	        Returns a list where the string has been split at each match
    sub	            Replaces one or many matches with a string
4. Metakarakter => karakter dengan arti khusus
    Character	Description	                                                                    Example
    []	        A set of characters	                                                                "[a-m]"
    \	        Signals a special sequence (can also be used to escape special characters)	        "\d"
    .	        Any character (except newline character)	                                        "he..o"
    ^	        Starts with	                                                                        "^hello"
    $	        Ends with	                                                                        "planet$"
    *	        Zero or more occurrences	                                                        "he.*o"
    +	        One or more occurrences	                                                            "he.+o"
    ?	        Zero or one occurrences	                                                            "he.?o"
    {}	        Exactly the specified number of occurrences	                                        "he.{2}o"
    |	        Either or	                                                                        "falls|stays"
    ()	        Capture and group
5. Special Sequences => Urutan khusus diikuti \ oleh salah satu karakter dalam daftar di bawah, dan memiliki arti khusus
    Character	Description	                                                                                                        Example
    \A	        Returns a match if the specified characters are at the beginning of the string	                                    "\AThe"
    \b	        Returns a match where the specified characters are at the beginning or at the end of a word                         r"\bain"
                (the "r" in the beginning is making sure that the string is being treated as a "raw string")	                    r"ain\b"
    \B	        Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word      r"\Bain"
                (the "r" in the beginning is making sure that the string is being treated as a "raw string")	                    r"ain\B"
    \d	Returns a match where the string contains digits (numbers from 0-9)	                                                        "\d"
    \D	Returns a match where the string DOES NOT contain digits	                                                                "\D"
    \s	Returns a match where the string contains a white space character	                                                        "\s"
    \S	Returns a match where the string DOES NOT contain a white space character	                                                "\S"
    \w	Returns a match where the string contains any word characters
        (characters from a to Z, digits from 0-9, and the underscore _ character)	                                                "\w"
    \W	Returns a match where the string DOES NOT contain any word characters	                                                    "\W"
    \Z	Returns a match if the specified characters are at the end of the string	                                                "Spain\Z"
6. Sets => sekumpulan karakter di dalam sepasang tKita kurung siku []yang mempunyai arti khusus
    Set	            Description
    [arn]	        Returns a match where one of the specified characters (a, r, or n) is present
    [a-n]	        Returns a match for any lower case character, alphabetically between a and n
    [^arn]	        Returns a match for any character EXCEPT a, r, and n
    [0123]	        Returns a match where any of the specified digits (0, 1, 2, or 3) are present
    [0-9]	        Returns a match for any digit between 0 and 9
    [0-5][0-9]	    Returns a match for any two-digit numbers from 00 and 59
    [a-zA-Z]	    Returns a match for any character alphabetically between a and z, lower case OR upper case
    [+]	            In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
7. Fungsi findall()
    a. Fungsi ini findall() mengembalikan list yang berisi semua kecocokan.
    b. List ini berisi kecocokan sesuai urutan penemuannya.
    c. Jika tidak ada kecocokan yang ditemukan, list kosong akan dikembalikan
8. Fungsi search()
    a. Fungsi ini search()mencari string yang cocok, dan mengembalikan objek Match jika ada yang cocok.
    b. Jika terdapat lebih dari satu kecocokan, hanya kemunculan kecocokan pertama yang akan dikembalikan
    c. Jika tidak ada kecocokan yang ditemukan, nilai Nonedikembalikan
9. Fungsi split()
    a. Fungsi ini split()mengembalikan daftar yang stringnya telah dipisahkan pada setiap kecocokan
    b. Kita dapat mengontrol jumlah kemunculan dengan menentukan maxsplit parameter
10. Fungsi sub()
    a. Fungsi ini sub()menggantikan kecocokan dengan teks pilihan Kita
    b. Kita dapat mengontrol jumlah penggantian dengan menentukan count parameter
11. Match Object => bjek yang berisi informasi tentang pencarian dan hasilnya
    a. Catatan: Jika tidak ada kecocokan, nilai Noneyang akan dikembalikan, bukan Match Object.
    b. Objek Match memiliki properti dan metode yang digunakan untuk mengambil informasi tentang pencarian, dan hasilnya:
        .span() => mengembalikan tupel yang berisi posisi awal dan akhir pertandingan.
        .string => mengembalikan string yang diteruskan ke fungsi
        .group() => mengembalikan bagian string yang cocok
"""
# 1. Contoh => Telusuri string untuk melihat apakah string tersebut dimulai dengan "The" dan diakhiri dengan "Spanyol"
import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

## 2. Fungsi findall()
# Cetak daftar semua kecocokan
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Kembalikan daftar kosong jika tidak ditemukan kecocokan
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

## 3. Fungsi search()
# Cari karakter spasi pertama dalam string
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# Lakukan pencarian yang tidak menghasilkan kecocokan
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

## 4. Fungsi split()
# Pisahkan pada setiap karakter spasi putih
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Pisahkan string hanya pada kemunculan pertama
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

## 5. Fungsi sub()
# Ganti setiap karakter spasi dengan angka 9
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Gantikan 2 kemunculan pertama

## 6. Match Object
# Lakukan pencarian yang akan mengembalikan Match Object
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object '<re.Match object; span=(5, 7), match='ai'>'

# Cetak posisi (posisi awal dan akhir) terjadinya kecocokan pertama.
# Ekspresi reguler mencari kata apa pun yang dimulai dengan huruf besar "S"
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# Cetak string yang diteruskan ke fungsi
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# Cetak bagian string yang ada kecocokannya.
# Ekspresi reguler mencari kata apa pun yang dimulai dengan huruf besar "S"
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

"""
Output yang Kita sebutkan adalah hasil dari eksekusi kode yang tepat. Mari kita lihat satu per satu:
1. print(x) mencetak objek kecocokan dari pencarian. Ini mencetak <re.Match object; span=(5, 7), match='ai'>, yang menunjukkan bahwa ditemukan kecocokan dengan kata "ai" pada posisi indeks 5 hingga 7 dalam string dan kata yang cocok adalah "ai".
2. print(x.span()) mencetak posisi (posisi awal dan akhir) dari kecocokan pertama. Karena Kita mencari kata yang dimulai dengan huruf besar "S" dan kata pertama yang sesuai adalah "Spain", posisi awal kecocokan adalah indeks 12 dan posisi akhirnya adalah indeks 17 dalam string.
3. print(x.string) mencetak string yang diteruskan ke fungsi pencarian. Dalam hal ini, itu adalah string asli "The rain in Spain".
4. print(x.group()) mencetak bagian string yang sesuai dengan pola pencarian. Karena pola pencarian mencari kata yang dimulai dengan huruf besar "S", dan kata pertama yang cocok adalah "Spain", maka hasilnya adalah "Spain".
"""