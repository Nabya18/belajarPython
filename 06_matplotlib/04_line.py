"""
Matplotlib Line

Gaya garis
    1. Kita dapat menggunakan kata kunci argument linestyle, atau short ls, untuk mengubah gaya garis yang diplot
    2. Gaya garis dapat ditulis dalam sintaks yang lebih pendek:
        - linestyle dapat ditulis sebagai ls.
        - dotted dapat ditulis sebagai :.
        - dashed dapat ditulis sebagai --.
    3. Kita dapat memilih salah satu gaya berikut:
        Style	                Or
        'solid' (default)	    '-'
        'dotted'	            ':'
        'dashed'	            '--'
        'dashdot'	            '-.'
        'None'	                '' or ' '
    4. Kita dapat menggunakan argumen kata kunci coloratau yang lebih pendek cuntuk mengatur warna garis
5. Kita dapat menggunakan argumen kata kunci linewidth atau lebih pendek lw untuk mengubah lebar garis.
6. Kita dapat memplot garis sebanyak yang Kita suka hanya dengan menambahkan lebih banyak plt.plot() fungsi
7. Kita juga dapat memplot banyak garis dengan menambahkan titik sumbu x dan y untuk setiap garis dalam plt.plot() fungsi yang sama.


"""
# Gunakan garis putus-putus - dotted
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

# Gunakan garis putus-putus - dashed
plt.plot(ypoints, linestyle = 'dashed')
plt.show()

# Sintaks yang lebih pendek
plt.plot(ypoints, ls = ':')
plt.show()

## Atur warna garis
# Atur warna garis menjadi merah
plt.plot(ypoints, color = 'r')
plt.show()

# Plot dengan garis hijau yang indah
plt.plot(ypoints, c = '#4CAF50')
plt.show()

# Plot dengan menggunakan warna nama yang didukung
plt.plot(ypoints, c = 'hotpink')
plt.show()

## Atur lebar garis
# Atur lebar garis menjadi 20
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20')
plt.show()

## Beberapa garis
# Gambarlah dua garis dengan menentukan plt.plot() fungsi untuk setiap baris
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

## Beberapa garis dengan titik
# Gambarlah dua garis dengan menentukan nilai titik x dan y untuk kedua garis
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()