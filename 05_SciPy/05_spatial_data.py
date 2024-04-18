"""
Data Spasial SciPy
    1. Data spasial mengacu pada data yang direpresentasikan dalam ruang geometris.
    2. SciPy memiliki modul yang disebut scipy.spatial yang mendukung operasi data spasial.
    3. Modul ini menyediakan fungsi untuk bekerja dengan data spasial, seperti jarak antara titik, poligon, dan lainnya.
    4. Beberapa fungsi yang disediakan oleh modul ini adalah:
        - distance: Menghitung jarak antara dua titik.
        - cKDTree: Membuat pohon KD untuk pencarian jarak terdekat.
        - ConvexHull: Membuat cangkang konveks dari sejumlah titik.
        - Delaunay: Membuat triangulasi Delaunay dari sejumlah titik.
        - Voronoi: Membuat diagram Vor

Triangulasi
    1. Triangulasi poligon adalah membagi poligon menjadi beberapa segitiga sehingga kita dapat menghitung luas poligon tersebut.
    2. Triangulasi dengan titik-titik berarti membuat segitiga-segitiga yang tersusun pada permukaan di mana semua titik-titik tertentu berada pada setidaknya satu titik sudut segitiga mana pun di permukaan tersebut.
    3. Salah satu metode untuk menghasilkan triangulasi melalui titik adalah Delaunay() Triangulasi.

Convex Hull
    1. ConvexHull adalah poligon terkecil yang menutupi semua titik tertentu.
    2. Gunakan ConvexHull() metode untuk membuat Convex Hull.

KDTrees
    1. KDTrees adalah struktur data yang dioptimalkan untuk kueri tetangga terdekat.
    2. Misalnya dalam sekumpulan titik dengan menggunakan KDTrees kita dapat secara efisien menanyakan titik mana yang paling dekat dengan titik tertentu.
    3. Metode ini KDTree() mengembalikan objek KDTree.
    4. Metode ini query() mengembalikan jarak ke tetangga terdekat dan lokasi tetangga.

Distance Matrix
    1. Ada banyak Metrik Jarak yang digunakan untuk mencari berbagai jenis jarak antara dua titik dalam ilmu data, jarak Euclidean, jarak kosinus, dll.
    2. Jarak antara dua vektor tidak hanya berupa panjang garis lurus di antara keduanya, tetapi juga dapat berupa sudut antara keduanya dari titik asal, atau jumlah satuan langkah yang diperlukan, dll.
    3. Banyak performa algoritme Machine Learning yang sangat bergantung pada metrik jarak. Misalnya "K Nearest Neighbors", atau "K Mean" dll.
        a. Euclidean Distance
            - Ini adalah jarak paling umum yang digunakan.
            - Ini adalah panjang garis
        b. Cityblock Distance (Manhattan Distance)
            - Apakah jarak dihitung dengan menggunakan 4 derajat pergerakan.
            - Misal kita hanya bisa bergerak: atas, bawah, kanan, atau kiri, tidak diagonal.
        c. Cosine Distance
            - Ini adalah jarak yang digunakan dalam ruang vektor.
            - Ini adalah sudut antara dua vektor.
            - Adalah nilai kosinus sudut antara dua titik A dan B.
        d. Hamming Distance
            - Adalah proporsi bit dimana dua bit berbeda.
            - Ini adalah cara mengukur jarak untuk barisan biner.

Berikut adalah ringkasan penggunaan fungsi dalam modul scipy.spatial:
    1. distance: Menghitung jarak antara dua titik. Digunakan dalam sistem rekomendasi, clustering, dan sistem navigasi.
    2. cKDTree: Membuat pohon KD untuk pencarian jarak terdekat. Digunakan dalam sistem rekomendasi, pencarian gambar, dan sistem navigasi.
    3. ConvexHull: Membuat cangkang konveks dari sejumlah titik. Digunakan dalam computer vision, analisis data spasial, dan game.
    4. Delaunay: Membuat triangulasi Delaunay dari sejumlah titik. Digunakan dalam computer vision, analisis data spasial, dan game.
    5. Voronoi: Membuat diagram Voronoi. Digunakan dalam analisis data spasial, sistem rekomendasi, dan game.
"""
# Buatlah triangulasi dari poin-poin berikut
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()

# Convex Hull
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()

# KDTrees
from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]

kdtree = KDTree(points)

res = kdtree.query((1, 1))

print(f"KdTree: {res}")

## Distance Matrix
# Euclidean Distance
from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)

res = euclidean(p1, p2)

print(f"Euclidean Distance: {res}")

# Cityblock Distance
from scipy.spatial.distance import cityblock

p1 = (1, 0)
p2 = (10, 2)

res = cityblock(p1, p2)

print(f"Cityblock Distance: {res}")

# Cosine Distance
from scipy.spatial.distance import cosine

p1 = (1, 0)
p2 = (10, 2)

res = cosine(p1, p2)

print(f"Cosine Distance: {res}")

# Hamming Distance
from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res = hamming(p1, p2)

print(f"Hamming Distance: {res}")