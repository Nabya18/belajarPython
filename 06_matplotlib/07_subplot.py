"""
subplot() fungsi ini Kita dapat menggambar banyak plot dalam satu gambar
1. Fungsi ini subplot()mengambil tiga argumen yang menggambarkan tata letak gambar.
2. Tata letaknya disusun dalam baris dan kolom, yang diwakili oleh argumen pertama dan kedua .
3. Argumen ketiga mewakili indeks plot saat ini.
    - Jadi, jika kita menginginkan gambar dengan 2 baris dan 1 kolom (artinya kedua plot tersebut akan ditampilkan di atas satu sama lain, bukan berdampingan)
    - Kita dapat menggambar plot sebanyak yang Kita suka pada satu gambar, cukup jelaskan jumlah baris, kolom, dan indeks plot.
4. title() fungsi untuk menambahkan judul setiap plot
5. suptitle() fungsi untuk menambahkan judul keseluruhan gambar.
"""
# Gambarlah 2 plot
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
"""
Indeks plot dalam fungsi subplot() digunakan untuk menentukan posisi plot dalam tata letak yang ditentukan oleh jumlah baris dan kolom. 
Indeks ini mengikuti urutan dari kiri ke kanan, dan dari atas ke bawah.  
Misalnya, jika Kita memiliki tata letak dengan 2 baris dan 2 kolom (membuat total 4 plot), indeks plot akan berjalan sebagai berikut:  
    Indeks 1: Plot pertama, di baris pertama dan kolom pertama.
    Indeks 2: Plot kedua, di baris pertama dan kolom kedua.
    Indeks 3: Plot ketiga, di baris kedua dan kolom pertama.
    Indeks 4: Plot keempat, di baris kedua dan kolom kedua.
Jadi, jika Kita ingin menggambar plot di posisi kedua, Kita akan menggunakan subplot(2, 2, 2).
"""

# Gambarlah 6 plot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()

# 2 petak, dengan judul
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.show()

# Tambahkan judul untuk keseluruhan gambar
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()