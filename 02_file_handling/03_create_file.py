"""
Menulis ke File yang Ada
Untuk menulis ke file yang sudah ada, Kita harus menambahkan parameter ke fungsi open():
"a"- Append - akan ditambahkan ke akhir file
"w"- Tulis - akan menimpa konten apa pun yang sudah ada

Buka file "demofile2.txt" dan tambahkan konten ke file:
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()

#open and read the file after the appending:
    f = open("demofile2.txt", "r")
    print(f.read())

Buka file "demofile3.txt" dan timpa isinya:
    f = open("demofile3.txt", "w")
    f.write("Woops! I have deleted the content!")
    f.close()

#open and read the file after the overwriting:
    f = open("demofile3.txt", "r")
    print(f.read())

Catatan: metode "w" akan menimpa seluruh file.

Buat File Baru
Untuk membuat file baru dengan Python, gunakan open()metode ini, dengan salah satu parameter berikut:
"x"- Create - akan membuat file, mengembalikan kesalahan jika file ada
"a"- Append - akan membuat file jika file yang ditentukan tidak ada
"w"- Write - akan membuat file jika file yang ditentukan tidak ada

Buat file bernama "myfile.txt":
    f = open("myfile.txt", "x")



"""
f = open("myfile.txt", "a")
f.write("Now the file has more content!")
f.close()