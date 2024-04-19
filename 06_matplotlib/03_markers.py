"""
Matplotlib Markers
Anda dapat menggunakan argumen kata kunci markeruntuk menekankan setiap titik dengan penanda tertentu

Referensi Penanda
    Deskripsi       Penanda
    'o'             Lingkaran
    '*'             Bintang
    '.'             Titik
    ','             Piksel
    'x'             X
    'X'             X (terisi)
    '+'             Ditambah
    'P'             Plus (terisi)
    's'             Kotak
    'D'             Berlian
    'd'             Berlian (tipis)
    'p'             Pentagon
    'H'             segi enam
    'h'             segi enam
    'v'             Segitiga Bawah
    '^'             Segitiga Atas
    '<'             Segitiga Kiri
    '>'             Segitiga Kanan
    '1'             ri Turun
    '2'             Tri Naik
    '3'             Tri Kiri
    '4'             Tri Benar
    '|'             Vline
    '_'             Garis

Memformat String fmt
    1. Kita juga dapat menggunakan parameter notasi string pintasan untuk menentukan penanda.
    2. Parameter ini juga disebut fmt, dan ditulis dengan sintaks berikut:
        marker|line|color
    3. Catatan: Jika Kita mengabaikan nilai garis di parameter fmt, tidak ada garis yang akan diplot.

Referensi Garis
    Line Syntax	        Description
    '-'	                Solid line
    ':'	                Dotted line
    '--'	            Dashed line
    '-.'	            Dashed/dotted line

Referensi Warna
    Color Syntax	    Description
    'r'	                Red
    'g'	                Green
    'b'	                Blue
    'c'	                Cyan
    'm'	                Magenta
    'y'	                Yellow
    'k'	                Black
    'w'	                White

Ukuran Penanda
    Kita dapat menggunakan argumen kata kunci markersizeatau versi yang lebih pendek, msuntuk mengatur ukuran penanda

Warna Penanda
    1. Kita dapat menggunakan argumen kata kunci markeredgecoloratau yang lebih pendek mecuntuk mengatur warna tepi penanda
    2. Kita dapat menggunakan argumen kata kunci markerfacecoloratau yang lebih pendek mfcuntuk mengatur warna di dalam tepi penanda
    3. Gunakan argumen mec dan mfc untuk mewarnai seluruh penanda
    4. Kita juga dapat menggunakan nilai warna heksadesimal, https://www.w3schools.com/colors/colors_hexadecimal.asp
    5. Atau salah satu dari 140 nama warna yang didukung, https://www.w3schools.com/colors/colors_names.asp
"""
# Tandai setiap titik dengan lingkaran
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

# Tandai setiap titik dengan bintang
plt.plot(ypoints, marker = '*')
plt.show()

# Tandai setiap titik dengan lingkaran dan warna biru
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:b')
plt.show()

# Atur ukuran penanda menjadi 20
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# Atur warna tepi penanda menjadi merah
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

# Atur warna di dalam tepi penanda menjadi merah
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

# Atur warna tepi dan di dalam penanda menjadi merah
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()

# Tandai setiap titik dengan warna hijau yang indah
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()

# Tandai setiap titik dengan warna bernama "hotpink"
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()