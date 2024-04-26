"""
bar() fungsi untuk menggambar grafik batang
1. Fungsi ini bar()mengambil argumen yang menjelaskan tata letak bilah.
2. Kategori dan nilainya diwakili oleh argumen pertama dan kedua sebagai array.

Batang Horizontal
    Jika Kita ingin bilah ditampilkan secara horizontal, bukan vertikal, gunakan fungsi barh()

Warna Batang
    kata kunci color untuk mengatur warna batang

Lebar Batang
    bar() argumen kata kunci widthuntuk mengatur lebar batang

Tinggi Batang
    barh() argumen kata kunci heightuntuk mengatur ketinggian batang
"""
## Gambar 4 batang
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

## Gambarlah 4 batang horizontal
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

## Gambar 4 batang merah
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red") # dapat menggunakan nama warna atau heksadesimal
plt.show()

## Atur lebar batang
# Gambarlah 4 batang yang sangat tipis
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

# Gambarlah 4 batang yang sangat tipis
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()