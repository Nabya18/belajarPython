"""
1. Distribusi Logistik digunakan untuk menggambarkan pertumbuhan.
2. Digunakan secara luas dalam pembelajaran mesin dalam regresi logistik, jaringan saraf, dll.
3. Ini memiliki tiga parameter:
    - loc- mean, di mana puncaknya. Bawaan 0.
    - scale- standard deviation, kerataan distribusi. Bawaan 1.
    - size- Bentuk array yang dikembalikan.

Perbedaan Antara Distribusi Logistik dan Normal
    1. Kedua distribusi tersebut hampir identik, namun distribusi logistik mempunyai wilayah yang lebih luas, yang berarti distribusi tersebut mewakili lebih banyak kemungkinan terjadinya suatu peristiwa yang jauh dari rata-rata.
    2. Untuk nilai skala yang lebih tinggi (deviasi standar), distribusi normal dan distribusi logistik hampir sama kecuali puncaknya.
"""
# Gambarkan sampel 2x3 dari distribusi logistik dengan mean 1 dan stddev 2.0
from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)

# Visualisasi Distribusi Logistik
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(size=1000), hist=False)

plt.show()

## Perbedaan Antara Distribusi Logistik dan Normal
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.legend()  # Menampilkan legenda
plt.show()

"""
Kode ini menghasilkan sampel acak dari distribusi logistik dengan parameter loc=1 dan scale=2, dalam bentuk array dengan ukuran (2, 3). 
Distribusi logistik adalah distribusi probabilitas yang sering digunakan dalam statistika dan teori probabilitas.

Parameter loc menentukan lokasi (pusat) distribusi, yaitu di mana nilai rata-rata atau median berada. 
Dalam kasus ini, nilai loc=1 menunjukkan bahwa distribusi tersebut memiliki pusat di 1.

Parameter scale mengontrol "skala" atau "besaran" distribusi, yang mengatur seberapa curam distribusinya. 
Semakin besar nilai scale, semakin curam distribusinya.

Dalam konteks aplikasi, distribusi logistik sering digunakan dalam pemodelan data yang memiliki ekor panjang di kedua arah, 
seperti dalam analisis keuangan, analisis risiko, dan pemodelan populasi.
"""