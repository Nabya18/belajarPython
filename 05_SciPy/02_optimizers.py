"""
Optimizers di Scipy
    Pengoptimal adalah serangkaian prosedur yang ditentukan dalam SciPy yang mencari nilai minimum suatu fungsi, atau akar persamaan.

Mengoptimalkan Fungsi
    Pada dasarnya, semua algoritma dalam Machine Learning tidak lebih dari sebuah persamaan kompleks yang perlu diminimalkan dengan bantuan data yang diberikan.

Akar Persamaan
    1. NumPy mampu mencari akar-akar polinomial dan persamaan linier, namun tidak dapat menemukan akar-akar persamaan non linier, seperti ini:
        x + cos(x)
    2. Untuk itu Anda bisa menggunakan fungsi SciPy optimize.root.
    3. Fungsi ini membutuhkan dua argumen yang diperlukan:
        fun - fungsi yang mewakili persamaan.
        x0 - tebakan awal untuk root.
    4. Fungsi ini mengembalikan objek dengan informasi mengenai solusinya.

Meminimalkan suatu Fungsi
    1. Suatu fungsi, dalam konteks ini, merepresentasikan sebuah kurva, kurva memiliki titik tinggi dan titik rendah .
    2. Titik tertinggi disebut maxima .
    3. Titik rendah disebut minimum .
    4. Titik tertinggi pada keseluruhan kurva disebut maxima global , sedangkan sisanya disebut maxima lokal .
    5. Titik terendah pada keseluruhan kurva disebut minimum global , sedangkan titik selebihnya disebut minimum lokal

Menemukan Minima
    1. Kita dapat menggunakan scipy.optimize.minimize() fungsi untuk meminimalkan fungsi.
    2. Fungsi ini minimize()mengambil argumen berikut:
        - fun - fungsi yang mewakili persamaan.
        - x0 - tebakan awal untuk root.
        - metode - nama metode yang akan digunakan. Nilai hukum:
            'CG'
            'BFGS'
            'Newton-CG'
            'L-BFGS-B'
            'TNC'
            'COBYLA'
            'SLSQP'
        - callback - fungsi dipanggil setelah setiap iterasi optimasi.
        - options - dict yang mendefinisikan parameter tambahan:
            {
                 "disp": boolean - print detailed description
                 "gtol": number - the tolerance of the error
              }
"""
# Mencari akar persamaan x + cos(x)
from scipy.optimize import root
import numpy as np

def eqn(x):
  return x + np.cos(x)

myroot = root(eqn, 0)

print(myroot.x)
"""
Catatan: Objek yang dikembalikan memiliki lebih banyak informasi tentang solusinya.
"""

# Cetak semua informasi tentang solusinya (bukan hanya xyang mana akar masalahnya)
print(f"myroot{myroot}")
"""
Fungsi root dari scipy.optimize mengembalikan sebuah objek yang berisi informasi lebih lengkap tentang solusi dari persamaan yang dicari akarnya, 
bukan hanya nilai akar itu sendiri. Informasi tambahan ini dapat berguna untuk analisis lebih lanjut atau debugging.  

Berikut adalah beberapa atribut penting dari objek yang dikembalikan oleh fungsi root:  
    x: Ini adalah solusi, atau akar, dari persamaan. Ini adalah nilai yang paling sering kita minati.  
    success: Sebuah boolean yang menunjukkan apakah algoritma berhasil menemukan akar atau tidak.  
    message: Pesan yang menjelaskan hasil dari algoritma. Misalnya, jika success adalah False, message ini dapat memberikan lebih banyak detail tentang apa yang salah.  
    fun: Nilai dari fungsi di x, idealnya ini harus mendekati 0 jika x adalah akar yang valid.  
    nfev: Jumlah evaluasi fungsi yang dilakukan oleh algoritma. Ini bisa memberikan gambaran tentang seberapa "mahal" algoritma ini dalam hal komputasi.  
    qtf: Nilai dari fungsi quasi-Newton di x.  

Dengan demikian, objek yang dikembalikan oleh root memberikan gambaran yang lebih lengkap tentang proses dan hasil dari pencarian akar, yang bisa sangat berguna tergantung pada kebutuhan Anda.
"""

# Minimalkan fungsi x^2 + x + 2 dengan BFGS
from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(f"mymin: {mymin}")