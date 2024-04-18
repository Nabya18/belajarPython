"""
Significance Tests
1. Dalam statistika, signifikansi statistik berarti bahwa hasil yang dihasilkan mempunyai alasan yang melatarbelakanginya, tidak dihasilkan secara acak atau kebetulan.
2. SciPy memberi kita modul bernama scipy.stats, yang memiliki fungsi untuk melakukan uji signifikansi statistik.
3. Berikut beberapa teknik dan kata kunci yang penting saat melakukan tes tersebut:
    a. Hipotesis dalam Statistik => Hipotesis adalah asumsi tentang suatu parameter dalam populasi.
        - Hipotesis Nol: Hipotesis yang diasumsikan benar atau Diasumsikan bahwa observasi tersebut tidak signifikan secara statistik.
        - Hipotesis alternatif: Diasumsikan bahwa pengamatan tersebut disebabkan oleh beberapa alasan.
            Contoh:
            Untuk penilaian seorang siswa kami akan mengambil:
                "siswa lebih buruk dari rata-rata" - sebagai hipotesis nol, dan:
                "siswa lebih baik dari rata-rata" - sebagai hipotesis alternatif.
        b. One tailed test => Jika hipotesis kita menguji satu sisi nilai saja, hal ini disebut "uji satu sisi".
        Contoh:
        Untuk hipotesis nol:
            "rata-ratanya sama dengan k", kita dapat memiliki hipotesis alternatif:
            "rata-ratanya kurang dari k", atau:
            "rata-ratanya lebih besar dari k"
    c. Two tailed test => Saat hipotesis kita menguji kedua sisi nilai.
        Contoh:
        Untuk hipotesis nol:
            "rata-ratanya sama dengan k", kita dapat memiliki hipotesis alternatif:
            "rata-ratanya tidak sama dengan k"
        Dalam hal ini meannya kurang dari, atau lebih besar dari k, dan kedua sisinya harus diperiksa.
    d. Alpha value => Nilai alpha merupakan tingkat signifikansi.
        Contoh:
            Seberapa dekat data tersebut dengan ekstrem agar hipotesis nol dapat ditolak.
            Biasanya diambil sebagai 0,01, 0,05, atau 0,1.
    e. P-value
        1. Nilai P menunjukkan seberapa dekat data tersebut dengan ekstrim.
        2. Nilai P dan nilai alpha dibandingkan untuk menentukan signifikansi statistik.
        3. Jika nilai p <= alpha kita menolak hipotesis nol dan mengatakan bahwa data tersebut signifikan secara statistik. jika tidak, kami menerima hipotesis nol.

T-Test
    1. Uji-t digunakan untuk menentukan apakah terdapat perbedaan yang signifikan antara rata-rata dua variabel dan memberi tahu kita apakah keduanya termasuk dalam distribusi yang sama.
    2. Ini adalah tes dua sisi.
    3. Fungsi ini ttest_ind() mengambil dua sampel dengan ukuran yang sama dan menghasilkan tupel statistik-t dan nilai-p.
    4. Jika Kita hanya ingin mengembalikan nilai p saja, gunakan properti pvalue

KS-Test
    1. Uji KS digunakan untuk memeriksa apakah nilai yang diberikan mengikuti suatu distribusi.
    2. Fungsi ini mengambil nilai yang akan diuji, dan CDF sebagai dua parameter.
    3. CDF dapat berupa string atau fungsi yang dapat dipanggil yang mengembalikan probabilitas.
    4. Ini dapat digunakan sebagai tes satu sisi atau dua sisi.
    5. Secara default, ini adalah dua sisi. Kita dapat meneruskan parameter alternatif sebagai string yang bersisi dua, lebih kecil, atau lebih besar.

Statistical Description of Data
    1. Untuk melihat ringkasan nilai dalam sebuah array, kita dapat menggunakan describe() fungsi tersebut.
    2. Ini mengembalikan deskripsi berikut:
        a. jumlah pengamatan (bangsawan)
        b. nilai minimum dan maksimum = minmax
        c. mean
        d. variance
        e. skewness
        f. kurtosis

Normality Tests (Skewness and Kurtosis)
    1. Uji normalitas didasarkan pada skewness dan kurtosis.
    2. Fungsi ini normaltest() mengembalikan nilai p untuk hipotesis nol:
    3. "x berasal dari distribusi normal" .
    a. Skewness: Skewness adalah ukuran ketidaksimetrisan distribusi data.
        Ukuran simetri dalam data.
        Untuk distribusi normal nilainya 0.
        Jika negatif berarti datanya condong ke kiri.
        Jika positif berarti datanya miring ke kanan.
    b. Kurtosis: Kurtosis adalah ukuran keberadaan ekor dalam distribusi data.
        Ukuran apakah data tersebut berat atau ringan yang mengarah ke distribusi normal.
        Kurtosis positif artinya berekor berat.
        Kurtosis negatif artinya berekor ringan.

Significance tests adalah metode statistik yang digunakan untuk memutuskan apakah suatu hasil dapat dianggap signifikan atau tidak. Dalam konteks aplikasi, significance tests sering digunakan dalam berbagai bidang seperti penelitian ilmiah, analisis data, machine learning, dan lainnya.  Berikut adalah beberapa contoh penggunaan significance tests dalam konteks aplikasi:
    1. A/B Testing: Dalam pengembangan web dan aplikasi, significance tests sering digunakan dalam A/B testing.
        Misalnya, jika Kita memiliki dua versi halaman web dan ingin mengetahui mana yang lebih efektif dalam menghasilkan klik atau konversi, Kita dapat menggunakan significance tests untuk menentukan apakah perbedaan antara dua versi tersebut signifikan atau hanya kebetulan.
    2. Machine Learning: Dalam machine learning, significance tests digunakan untuk membandingkan performa dari dua atau lebih model.
        Misalnya, jika Kita memiliki beberapa model klasifikasi dan ingin mengetahui mana yang lebih baik, Kita dapat menggunakan significance tests untuk menentukan apakah perbedaan performa antara model tersebut signifikan atau tidak.
    3. Penelitian Ilmiah: Dalam penelitian ilmiah, significance tests digunakan untuk menentukan apakah hasil penelitian (misalnya, perbedaan antara grup kontrol dan grup eksperimental) signifikan atau tidak.
        Ini membantu peneliti untuk menarik kesimpulan dari data mereka dan menentukan apakah hipotesis mereka benar atau tidak.
    4. Analisis Data: Dalam analisis data, significance tests digunakan untuk menentukan apakah suatu pola dalam data (misalnya, korelasi antara dua variabel) signifikan atau hanya kebetulan.
        Ini membantu analis data untuk membuat keputusan berdasarkan data mereka.
Dalam semua kasus ini, significance tests memberikan kerangka kerja untuk membuat keputusan berdasarkan data, dan membantu untuk membedakan antara hasil yang signifikan dan yang mungkin hanya terjadi karena kebetulan.
"""
# Temukan apakah nilai yang diberikan v1 dan v2 berasal dari distribusi yang sama:
import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)

# mengembalikan nilai p saja
res = ttest_ind(v1, v2).pvalue

print(res)

## KS-Test
# Temukan apakah nilai yang diberikan mengikuti distribusi normal
import numpy as np
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')

print(res)

## Deskripsi Statistik
# Tampilkan deskripsi statistik dari nilai dalam array
import numpy as np
from scipy.stats import describe

v = np.random.normal(size=100)
res = describe(v)

print(res)

## Uji Normalitas
# Temukan kemiringan dan kurtosis nilai dalam array:
import numpy as np
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))

# Temukan apakah datanya berasal dari distribusi normal:
import numpy as np
from scipy.stats import normaltest

v = np.random.normal(size=100)

print(normaltest(v))