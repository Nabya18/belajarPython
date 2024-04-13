"""
Normal (Gaussian) Distribution
    1. Distribusi Normal adalah salah satu distribusi yang paling penting.
    2. Distribusi ini juga disebut Distribusi Gaussian yang diambil dari nama matematikawan Jerman Carl Friedrich Gauss.
    3. Ini sesuai dengan distribusi probabilitas dari banyak peristiwa, misalnya. Skor IQ, Detak Jantung, dll.
    4. Gunakan random.normal()cara tersebut untuk mendapatkan Distribusi Data Normal.

Ini memiliki tiga parameter:
    1. loc- (Mean) dimana puncak loncengnya berada.
    2. scale- (Standard Deviation) seberapa datar seharusnya distribusi grafik.
    3. size- Bentuk array yang dikembalikan.

Catatan: Kurva Distribusi Normal disebut juga Kurva Lonceng karena kurvanya berbentuk lonceng.
"""
# Hasilkan distribusi normal acak ukuran 2x3
from numpy import random

x = random.normal(size=(2, 3))

print(x)


# Hasilkan distribusi normal acak berukuran 2x3 dengan mean 1 dan deviasi standar 2
x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)


## Visualisasi Distribusi Normal
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show()

"""
Dalam konteks aplikasi, distribusi normal sering digunakan dalam berbagai bidang, termasuk:
    1. Ilmu Sosial dan Perilaku Manusia: Dalam psikologi, sosiologi, dan ilmu sosial lainnya, distribusi normal digunakan untuk memodelkan berbagai variabel, seperti kecerdasan, skor tes, dan perilaku manusia lainnya.
    2. Ekonomi dan Keuangan: Distribusi normal sering digunakan dalam analisis ekonomi dan keuangan untuk memodelkan variabel seperti harga aset keuangan, pendapatan, dan return investasi.
    3. Kesehatan: Dalam bidang kesehatan, distribusi normal digunakan untuk memodelkan variabel seperti tinggi badan, berat badan, dan tekanan darah dalam populasi.
    4. Ilmu Alam: Dalam fisika, biologi, dan ilmu alam lainnya, distribusi normal sering digunakan untuk memodelkan berbagai fenomena, seperti distribusi energi molekuler, distribusi populasi organisme, dan variasi alamiah dalam data pengukuran.
    5. Pengendalian Kualitas: Dalam pengendalian kualitas dan manufaktur, distribusi normal digunakan dalam analisis statistik untuk memantau proses produksi dan mengidentifikasi penyimpangan dari standar kualitas yang ditetapkan.
    6. Analisis Risiko dan Asuransi: Dalam analisis risiko dan perencanaan asuransi, distribusi normal sering digunakan untuk memodelkan variasi risiko dan menghitung premi asuransi.
    7. Analisis Data dan Machine Learning: Dalam analisis data dan machine learning, distribusi normal sering digunakan sebagai asumsi dasar dalam berbagai teknik analisis, seperti regresi linear, analisis komponen utama (PCA), dan algoritma pembelajaran statistik lainnya.
"""