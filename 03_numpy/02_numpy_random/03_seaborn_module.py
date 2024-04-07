"""
Visualisasikan Distribusi Dengan Seaborn
    1. Seaborn adalah perpustakaan yang menggunakan Matplotlib di bawahnya untuk memplot grafik.
    2. Ini akan digunakan untuk memvisualisasikan distribusi acak.

Displot
    Distplot adalah singkatan dari plot distribusi,
    yang mengambil input array dan memplot kurva yang sesuai dengan distribusi titik-titik dalam array.

Catatan: Kita akan menggunakan: sns.distplot(arr, hist=False) untuk memvisualisasikan distribusi acak dalam tutorial ini.
"""
# Plotting a Distplot
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()


# Plotting a Distplot Without the Histogram
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()