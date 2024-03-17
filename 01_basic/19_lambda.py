"""
Fungsi lambda => adalah fungsi anonim kecil.
Fungsi lambda dapat mengambil sejumlah argumen, namun hanya dapat memiliki satu ekspresi.
Lambda digunakan untuk membuat fungsi kecil atau sementara dalam kode tanpa perlu mendefinisikan fungsi secara terpisah menggunakan kata kunci def.

syntax
lambda arguments : expression

Manfaat fungsi lambda:
1. Ringkasan Kode: Lambda memungkinkan penulisan fungsi dalam satu baris kode, membuatnya lebih ringkas dibandingkan dengan pendekatan tradisional menggunakan def.
2. Pemrograman Fungsional: Lambda mendukung paradigma pemrograman fungsional di Python, digunakan bersama dengan fungsi built-in seperti map(), filter(), dan reduce(), serta dalam ekspresi list dan dictionary comprehension.
3. Fleksibilitas: Lambda bermanfaat ketika kita membutuhkan fungsi kecil sebagai argumen untuk fungsi lain, seperti dalam fungsi map().
4. Tidak Memerlukan Nama: Karena lambda adalah fungsi anonim, kita tidak perlu memikirkan nama untuk fungsi tersebut, berguna saat kita hanya perlu menggunakan fungsi itu dalam satu tempat tertentu.
5. Ekspresi Inline: Lambda memungkinkan kita mendefinisikan fungsi secara langsung di dalam ekspresi di mana fungsi tersebut digunakan,
6. Penggunaan Memori yang Lebih Efisien: Karena lambda adalah fungsi anonim, mereka tidak diberi nama atau disimpan di memori setelah pemanggilan

Gunakan fungsi lambda ketika fungsi anonim diperlukan untuk jangka waktu singkat.
"""

# contoh: Tambahkan 10 ke argument a, dan kembalikan hasilnya:
x = lambda a : a + 10
print(x(5))

# contoh: Lipat gandakan argumen adengan argumen b dan kembalikan hasilnya:
x = lambda a, b : a * b
print(x(5, 6))

# contoh: Ringkas argumen a, b, dan cdan kembalikan hasilnya:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# contoh: membuat fungsi yang selalu menggandakan jumlah yang kita kirimkan
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2) # n

print(mydoubler(11)) # a