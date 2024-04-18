"""
SciPy Interpolation
    1. Interpolasi adalah metode untuk menghasilkan titik di antara titik-titik tertentu.
    2. Misalnya: untuk poin 1 dan 2, kita dapat melakukan interpolasi dan menemukan poin 1,33 dan 1,66.
    3. Interpolasi memiliki banyak kegunaan, dalam Machine Learning kita sering menangani data yang hilang dalam suatu dataset, interpolasi sering digunakan untuk menggantikan nilai-nilai tersebut.
    4. Metode pengisian nilai ini disebut imputasi .
    5. Selain imputasi, interpolasi sering digunakan ketika kita perlu memuluskan titik-titik diskrit dalam kumpulan data.
    6. SciPy menyediakan modul scipy.interpolate untuk melakukan interpolasi.

1D Interpolation
    1. Fungsi tersebut interp1d() digunakan untuk menginterpolasi suatu distribusi dengan 1 variabel.
    2. Dibutuhkan x dan y menunjuk serta mengembalikan fungsi yang dapat dipanggil yang dapat dipanggil dengan new xdan mengembalikan fungsi yang sesuai y.

Spline Interpolation
    1. Dalam interpolasi 1D, titik-titik dipasang pada kurva tunggal sedangkan pada interpolasi Spline, titik-titik dipasang pada piecewise function yang ditentukan dengan polinomial yang disebut splines.
    2. Fungsi tersebut UnivariateSpline() mengambil xs dan ys dan menghasilkan fungsi yang dapat dipanggil yang dapat dipanggil dengan new xs.
    3. Piecewise function: Fungsi yang memiliki definisi berbeda untuk rentang berbeda.

Interpolation with Radial Basis Function
    1. Fungsi basis radial adalah fungsi yang didefinisikan sesuai dengan titik acuan tetap.
    2. Fungsi tersebut Rbf() juga menggunakan xs dan ys sebagai argumen dan menghasilkan fungsi yang dapat dipanggil yang dapat dipanggil dengan new xs.


"""
# Untuk nilai interpolasi xs dan ys tertentu dari 2.1, 2.2... hingga 2.9
from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)
"""
Catatan: xs baru harus berada dalam rentang yang sama dengan xs lama, artinya kita tidak dapat memanggil interp_func() dengan nilai lebih tinggi dari 10, atau kurang dari 0.

Interpolasi 1D (interp1d): Fungsi ini melakukan interpolasi linier (default) antara titik-titik yang diberikan. Dalam kasus Kita, xs adalah array dari 0 hingga 9 dan ys adalah 2 kali xs ditambah 1. 
Jadi, ketika Kita meminta nilai interpolasi antara 2.1 dan 2.9, Kita mendapatkan nilai yang sesuai dengan fungsi linier y = 2x + 1.
"""

# Temukan interpolasi spline univariat untuk 2.1, 2.2... 2.9 untuk titik-titik non linier berikut
from scipy.interpolate import UnivariateSpline
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)
"""
Interpolasi Spline Univariat (UnivariateSpline): Fungsi ini melakukan interpolasi spline pada titik-titik yang diberikan. 
Dalam kasus Kita, ys adalah xs kuadrat ditambah sinus xs ditambah 1. 
Jadi, ketika Kita meminta nilai interpolasi antara 2.1 dan 2.9, Kita mendapatkan nilai yang sesuai dengan fungsi spline yang dibentuk oleh ys.
"""

# Interpolasi xs dan ys berikut menggunakan rbf dan temukan nilai untuk 2.1, 2.2 ... 2.9
from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)
"""
Interpolasi dengan Fungsi Basis Radial (Rbf): Fungsi ini melakukan interpolasi menggunakan fungsi basis radial. 
Dalam kasus Kita, ys adalah sama dengan kasus sebelumnya. 
Jadi, ketika Kita meminta nilai interpolasi antara 2.1 dan 2.9, Kita mendapatkan nilai yang sesuai dengan fungsi basis radial yang dibentuk oleh ys.
"""