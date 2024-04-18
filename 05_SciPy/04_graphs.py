"""
Graphics
    1. Grafik adalah struktur data yang penting.
    2. SciPy memberi kita modul scipy.sparse.csgraph untuk bekerja dengan struktur data tersebut.

Adjacency Matrix
    1. Matriks ketetanggaan adalah nxnmatriks yang n merupakan jumlah elemen dalam suatu graf.
    2. Dan nilai-nilai tersebut mewakili hubungan antar elemen.
    3. Berikut ini beberapa metode yang paling sering digunakan untuk bekerja dengan Adjacency Matrix:
        - Connected Components
            a. Metode connected_components() metode ini digunakan untuk menemukan komponen terhubung dalam graf.
            b. Dalam graf yang tidak terhubung, setiap komponen terhubung adalah subgraf di mana setiap dua verteks terhubung satu sama lain oleh jalur, dan yang tidak terhubung ke verteks tambahan di subgraf lain.
        - Dijkstra
            a. Gunakan dijkstrametode ini untuk menemukan jalur terpendek dalam grafik dari satu elemen ke elemen lainnya.
            b. Dibutuhkan argumen berikut:
                > return_predecessors: boolean (Benar untuk mengembalikan seluruh jalur traversal jika tidak, Salah).
                > indices: indeks elemen untuk mengembalikan semua jalur dari elemen itu saja.
                > limit: berat jalur maksimal.
        - Floyd Warshall
            Gunakan floyd_warshall() metode ini untuk menemukan jalur terpendek antara semua pasangan elemen.
        - Bellman Ford
            Metode ini bellman_ford()juga dapat menemukan jalur terpendek antara semua pasangan elemen, namun metode ini juga dapat menangani bobot negatif.
        - Depth First Order
            a. Metode ini depth_first_order() mengembalikan traversal kedalaman pertama dari sebuah node.
            b. Fungsi ini mengambil argumen berikut:
                > grafik.
                > elemen awal untuk melintasi grafik dari.
        - Breadth First Order
            a. Metode ini breadth_first_order()mengembalikan traversal pertama yang luas dari sebuah node.
            b. Fungsi ini mengambil argumen berikut:
            > grafik.
            > elemen awal untuk melintasi grafik dari.

Dalam konteks aplikasi, graf digunakan dalam berbagai bidang dan memiliki banyak penggunaan praktis. Berikut adalah beberapa contoh:
  1. Jaringan Sosial: Graf digunakan untuk merepresentasikan jaringan sosial, di mana individu direpresentasikan sebagai simpul dan hubungan antara mereka direpresentasikan sebagai tepi.
      Algoritma seperti Depth-First Search (DFS) atau Breadth-First Search (BFS) dapat digunakan untuk menemukan koneksi antara individu atau untuk menemukan komunitas dalam jaringan.
  2. Sistem Rekomendasi: Graf juga digunakan dalam sistem rekomendasi, di mana item direpresentasikan sebagai simpul dan hubungan antara item (seperti rating yang sama oleh pengguna atau dibeli bersama) direpresentasikan sebagai tepi.
      Algoritma seperti Dijkstra atau Floyd Warshall dapat digunakan untuk menemukan item yang paling mirip dengan item yang disukai oleh pengguna.
  3. Routing dan Navigasi: Graf digunakan dalam aplikasi routing dan navigasi, di mana lokasi direpresentasikan sebagai simpul dan jalan atau jalur antara lokasi direpresentasikan sebagai tepi.
      Algoritma seperti Dijkstra atau Bellman Ford dapat digunakan untuk menemukan rute terpendek antara dua lokasi.
  4. Optimasi Jaringan: Dalam bidang seperti telekomunikasi atau logistik, graf digunakan untuk merepresentasikan jaringan, di mana simpul mewakili titik seperti pusat data atau gudang, dan tepi mewakili koneksi seperti kabel serat optik atau rute pengiriman.
      Algoritma seperti Floyd Warshall atau Bellman Ford dapat digunakan untuk optimasi jaringan, seperti menemukan jalur terpendek antara semua pasangan simpul atau menemukan jalur terpendek yang memungkinkan bobot negatif.
  5. Analisis Web: Graf digunakan dalam analisis web, di mana halaman web direpresentasikan sebagai simpul dan tautan antara halaman web direpresentasikan sebagai tepi.
      Algoritma seperti Depth-First Search (DFS) atau Breadth-First Search (BFS) dapat digunakan untuk meramban web atau untuk menemukan komponen terhubung dalam web.
"""
# Connected Components
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))
"""
Ini berarti bahwa simpul 0 terhubung ke simpul 1 dan 2, simpul 1 terhubung ke simpul 0, dan simpul 2 terhubung ke simpul 0. Dengan kata lain, semua simpul terhubung satu sama lain, membentuk satu komponen terhubung.  
Fungsi connected_components mengembalikan dua nilai:  
    1. Jumlah komponen terhubung dalam graf.
    2. Array yang menunjukkan komponen terhubung mana yang termasuk setiap simpul.
Dalam hal ini, ada satu komponen terhubung (sehingga output pertama adalah 1), dan semua simpul termasuk dalam komponen terhubung yang sama (sehingga output kedua adalah array([0, 0, 0]), yang berarti bahwa sim
"""

# Dijkstra
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(dijkstra(newarr, return_predecessors=True, indices=0))
"""
1. Hasil tersebut berasal dari fungsi dijkstra dari modul scipy.sparse.csgraph. 
2. Fungsi ini digunakan untuk menemukan jalur terpendek dalam graf dari satu elemen ke elemen lainnya.  
3. Fungsi dijkstra mengembalikan dua array:  
    a. Array pertama adalah array jarak terpendek dari simpul awal (dalam hal ini, simpul 0) ke semua simpul lainnya. 
        Dalam kasus Kita, array ini adalah [0., 1., 2.], yang berarti jarak terpendek dari simpul 0 ke simpul 0 adalah 0, dari simpul 0 ke simpul 1 adalah 1, dan dari simpul 0 ke simpul 2 adalah 2.  
    b. Array kedua adalah array pendahulu, yang menunjukkan simpul sebelumnya di jalur terpendek dari simpul awal ke simpul lainnya. 
        Nilai -9999 biasanya menunjukkan bahwa tidak ada pendahulu (seperti dalam kasus simpul awal). Dalam kasus Kita, array ini adalah [-9999, 0, 0], yang berarti bahwa untuk mencapai simpul 1 dan 2 dari simpul 0, simpul sebelumnya adalah simpul 0.
"""

# Floyd Warshall
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(floyd_warshall(newarr, return_predecessors=True))
"""
1. Hasil tersebut berasal dari fungsi floyd_warshall dari modul scipy.sparse.csgraph. 
2. Fungsi ini digunakan untuk menemukan jalur terpendek antara semua pasangan simpul dalam graf.  
3. Fungsi floyd_warshall mengembalikan dua array:
    a. Array pertama adalah matriks jarak terpendek antara setiap pasangan simpul. Dalam kasus Kita, matriks ini adalah:
        [[0. 1. 2.]
         [1. 0. 3.]
         [2. 3. 0.]]
        yang berarti jarak terpendek dari simpul 0 ke simpul 0 adalah 0, dari simpul 0 ke simpul 1 adalah 1, dari simpul 0 ke simpul 2 adalah 2, dan seterusnya.
    
    b. Array kedua adalah matriks pendahulu, yang menunjukkan simpul sebelumnya di jalur terpendek antara setiap pasangan simpul. 
        Nilai -9999 biasanya menunjukkan bahwa tidak ada pendahulu. Dalam kasus Kita, matriks ini adalah:
            [[-9999     0     0]
             [    1 -9999     0]
             [    2     0 -9999]]
        yang berarti bahwa untuk mencapai simpul 1 dari simpul 0, simpul sebelumnya adalah simpul 0, untuk mencapai simpul 2 dari simpul 1, simpul sebelumnya adalah simpul 0, dan seterusnya.
"""

# Bellman Ford
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors=True, indices=0))
"""
1. Hasil tersebut berasal dari fungsi bellman_ford dari modul scipy.sparse.csgraph. 
2. Fungsi ini digunakan untuk menemukan jalur terpendek dari satu simpul ke semua simpul lainnya dalam graf berarah berbobot. 
3. Algoritma ini dapat menangani bobot negatif.  Fungsi bellman_ford mengembalikan dua array:  
    a. Array pertama adalah array jarak terpendek dari simpul awal (dalam hal ini, simpul 0) ke semua simpul lainnya. 
        Dalam kasus Kita, array ini adalah [0., -1., 2.], yang berarti jarak terpendek dari simpul 0 ke simpul 0 adalah 0, dari simpul 0 ke simpul 1 adalah -1 (mengingat bobot negatif diperbolehkan), dan dari simpul 0 ke simpul 2 adalah 2.  
    
    b. Array kedua adalah array pendahulu, yang menunjukkan simpul sebelumnya di jalur terpendek dari simpul awal ke simpul lainnya. 
        Nilai -9999 biasanya menunjukkan bahwa tidak ada pendahulu (seperti dalam kasus simpul awal). 
        Dalam kasus Kita, array ini adalah [-9999, 0, 0], yang berarti bahwa untuk mencapai simpul 1 dan 2 dari simpul 0, simpul sebelumnya adalah simpul 0.
"""

# Depth First Order
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))
"""
1. Hasil tersebut berasal dari fungsi depth_first_order dari modul scipy.sparse.csgraph. 
2. Fungsi ini digunakan untuk melakukan traversal kedalaman pertama dari sebuah simpul dalam graf.  Fungsi depth_first_order mengembalikan dua array:  
    a. Array pertama adalah array simpul dalam urutan mereka dikunjungi oleh traversal kedalaman pertama. 
        Dalam kasus Kita, array ini adalah [1, 0, 3, 2], yang berarti simpul 1 dikunjungi pertama, diikuti oleh simpul 0, kemudian simpul 3, dan terakhir simpul 2.  
    
    b. Array kedua adalah array pendahulu, yang menunjukkan simpul sebelumnya di jalur traversal kedalaman pertama. 
        Nilai -9999 biasanya menunjukkan bahwa tidak ada pendahulu (seperti dalam kasus simpul awal). 
        Dalam kasus Kita, array ini adalah [1, -9999, 1, 0], yang berarti bahwa untuk mencapai simpul 0 dan 2 dari simpul 1, simpul sebelumnya adalah simpul 1, dan untuk mencapai simpul 3 dari simpul 0, simpul sebelumnya adalah simpul 0.
"""

# Breadth First Order
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))
"""
1. Hasil tersebut berasal dari fungsi breadth_first_order dari modul scipy.sparse.csgraph. 
2. Fungsi ini digunakan untuk melakukan traversal lebar pertama (breadth-first traversal) dari sebuah simpul dalam graf.  Fungsi breadth_first_order mengembalikan dua array:  
    a. Array pertama adalah array simpul dalam urutan mereka dikunjungi oleh traversal lebar pertama. 
        Dalam kasus Kita, array ini adalah [1, 0, 2, 3], yang berarti simpul 1 dikunjungi pertama, diikuti oleh simpul 0, kemudian simpul 2, dan terakhir simpul 3.  
    
    b. Array kedua adalah array pendahulu, yang menunjukkan simpul sebelumnya di jalur traversal lebar pertama. Nilai -9999 biasanya menunjukkan bahwa tidak ada pendahulu (seperti dalam kasus simpul awal). 
        Dalam kasus Kita, array ini adalah [1, -9999, 1, 1], yang berarti bahwa untuk mencapai simpul 0, 2, dan 3 dari simpul 1, simpul sebelumnya adalah simpul 1.
"""