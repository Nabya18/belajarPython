"""
Pandas - Plotting

Plotting => Pandas menggunakan metode plot() untuk membuat diagram dari data yang ada.
    1. Diagram adalah cara yang bagus untuk membuat data lebih informatif dan lebih mudah dipahami.
    2. Pandas menggunakan library Matplotlib untuk membuat diagram.
    3. Diagram yang paling umum adalah diagram garis.
    4. Diagram garis sangat baik saat Kita ingin menunjukkan bagaimana nilai berubah seiring waktu.
    5. Untuk membuat diagram garis, Kita dapat menggunakan plot() metode dengan parameter kind = 'line'.

Scatter Plot => kind = 'scatter'
    1. Diagram sebar adalah cara yang bagus untuk menunjukkan hubungan antara dua set data.
    2. Pandas menggunakan plot() metode dengan parameter kind = 'scatter' untuk membuat diagram sebar
    3. Plot sebar memerlukan sumbu x dan y.

Histogram => kind = 'hist'
    1. Diagram histogram adalah cara yang bagus untuk menunjukkan distribusi frekuensi.
    2. Pandas menggunakan plot() metode dengan parameter kind = 'hist' untuk membuat diagram histogram.
    3. Diagram histogram hanya memerlukan satu kolom.
"""
# Impor pyplot dari Matplotlib dan visualisasikan DataFrame
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

## scatter plot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()
"""
kita mengetahui bahwa korelasi antara "Durasi" dan "Kalori" adalah 0.922721, 
dan kita menyimpulkan dengan fakta bahwa durasi yang lebih tinggi berarti lebih banyak kalori yang terbakar.
"""

# scatter plot di mana tidak ada hubungan antar kolom
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()

## Histogram
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df["Duration"].plot(kind = 'hist')

plt.show()
"""
Catatan: Histogram memberi tahu kita bahwa ada lebih dari 100 latihan yang berlangsung antara 50 dan 60 menit.
"""