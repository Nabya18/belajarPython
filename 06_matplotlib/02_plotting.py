"""
Plot Matplotlib
    1. Fungsi tersebut plot()digunakan untuk menggambar titik (penKita) dalam diagram.
    2. Secara default, plot()fungsi ini menggambar garis dari titik ke titik.
    3. Fungsi ini mengambil parameter untuk menentukan titik-titik dalam diagram.
        - Parameter 1 adalah array yang berisi titik-titik pada sumbu x .
        - Parameter 2 adalah array yang berisi titik-titik pada sumbu y .
        Jika kita perlu memplot garis dari (1, 3) hingga (8, 10), kita harus meneruskan dua larik [1, 8] dan [3, 10] ke fungsi plot.

Plotting Without Line
    Untuk memplot penKita saja, Kita dapat menggunakan parameter notasi string pintasan 'o', yang berarti 'rings'.

Multiple Points
    Kita dapat memplot titik sebanyak yang Kita suka, namun pastikan Kita memiliki jumlah titik yang sama di kedua sumbu.

Poin X Default
    1. Poin X default merujuk pada perilaku fungsi plot() dari Matplotlib ketika hanya satu array yang diberikan sebagai argumen.
    2. Jika hanya satu array yang diberikan, fungsi plot() akan menganggap array tersebut sebagai nilai-nilai pada sumbu Y,
    3. dan akan secara otomatis membuat array untuk sumbu X dengan nilai yang sama dengan indeks dari setiap elemen dalam array Y.
    4. Misalnya, jika Kita memiliki array Y seperti ini: [3, 8, 1, 10], dan Kita memanggil plot(ypoints), maka Matplotlib akan secara otomatis membuat array X sebagai [0, 1, 2, 3, dst.].
    5. Jadi, poin-poin yang akan diplot adalah (0,3), (1,8), (2,1), dan (3,10).

"""
# Gambarlah garis pada diagram dari posisi (1,3) ke posisi (8,10)
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

## Plotting Without Line
# Gambarlah penKita pada diagram dari posisi (1,3) dan (8,10)
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

## Multiple Points
# Gambarlah garis pada diagram dari posisi (1,3) ke posisi (2,8) ke posisi (6,1) ke posisi (8,10)
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

## Poin X Default
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
"""
Dalam kode di atas, karena hanya satu array yang diberikan ke fungsi plot(), maka fungsi tersebut akan membuat array X secara otomatis dengan nilai [0, 1, 2, 3].
"""