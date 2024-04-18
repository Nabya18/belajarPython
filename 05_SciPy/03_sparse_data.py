"""
1. Sparse data adalah data yang memiliki banyak nilai nol.
2. Ini bisa berupa array seperti ini:
    [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]
3. Dense Array adalah array yang sebagian besar nilainya tidak nol .
4. Dalam komputasi ilmiah, ketika kita berurusan dengan turunan parsial dalam aljabar linier, kita akan menemukan sparse data.
5. SciPy memiliki modul yang disebut scipy.sparse yang mendukung operasi matriks sparse.
6. Ada beberapa jenis matriks sparse yang didukung oleh SciPy:
    1. csc_matrix: Kolom Jarang Terkompresi. Untuk aritmatika yang efisien, pemotongan kolom yang cepat.
    2. csr_matrix: Baris Jarang Terkompresi. Untuk pemotongan baris yang cepat, produk vektor matriks yang lebih cepat
    3. lil_matrix: List of Lists format
    4. dok_matrix: Dictionary of Keys format
    5. coo_matrix: COOrdinate format
    6. bsr_matrix: Block Sparse Row format
    7. dia_matrix: DIAgonal format
    8. csc_matrix: Compressed Sparse Column format
    9. dia_matrix: DIAgonal format
    10. dok_matrix: Dictionary Of Keys format
    11. lil_matrix: List of Lists format
    12. coo_matrix: COOrdinate format
    13. bsr_matrix: Block Sparse Row format
    14. csr_matrix: Compressed Sparse Row format
    15. csc_matrix: Compressed Sparse Column format
    16. dia_matrix: DIAgonal format
    17. dok_matrix: Dictionary Of Keys format
    18. lil_matrix: List of Lists format
    19. coo_matrix: COOrdinate format
    20. bsr_matrix: Block Sparse Row format
    21. csr_matrix: Compressed Sparse Row format
    22. csc_matrix: Compressed Sparse Column format
    23. dia_matrix: DIAgonal format
    24. dok_matrix: Dictionary Of Keys format
    25. lil_matrix: List of Lists format
    26. coo_matrix: COOrdinate format
    27. bsr_matrix: Block Sparse Row format
    28. csr_matrix: Compressed Sparse Row format
    29. csc_matrix: Compressed Sparse Column format
    30. dia_matrix: DIAgonal format
    31. dok_matrix: Dictionary Of Keys format
    32. lil_matrix: List of Lists format
    33. coo_matrix: COOrdinate format
    34. bsr_matrix: Block Sparse Row format
    35. csr_matrix: Compressed Sparse Row format
    36. csc_matrix: Compressed Sparse Column format
    37. dia_matrix: DIAgonal format
    38. dok_matrix: Dictionary Of Keys format
7. Menghitung angka bukan nol dengan count_nonzero() metode
8. Menghapus entri nol dari matriks dengan eliminate_zeros() metode
9. Menghilangkan duplikat entri dengan sum_duplicates() metode
10. Konversi dari csr ke csc dengan tocsc() metode
"""
# Buat matriks CSR dari array
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))
"""
Output tersebut adalah representasi dari matriks sparse dalam format CSR (Compressed Sparse Row). 
Format ini efisien dalam hal memori dan komputasi untuk matriks yang sebagian besar elemennya adalah nol.  
Berikut penjelasan output tersebut:  
    (0, 5) 1: Ini berarti bahwa ada elemen dengan nilai 1 pada baris 0 dan kolom 5.
    (0, 6) 1: Ini berarti bahwa ada elemen dengan nilai 1 pada baris 0 dan kolom 6.
    (0, 8) 2: Ini berarti bahwa ada elemen dengan nilai 2 pada baris 0 dan kolom 8.
    
Elemen lainnya dalam matriks tidak ditampilkan karena nilainya adalah 0. 
Dengan cara ini, matriks sparse dapat menghemat memori dan mempercepat komputasi dengan hanya menyimpan dan memproses elemen-elemen yang bukan nol.
"""

## Sparse Matrix Methods
# Melihat data yang disimpan (bukan item nol) dengan data properti
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)

# Menghitung angka bukan nol
print(csr_matrix(arr).count_nonzero())

# Menghapus entri nol dari matriks
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)
mat.eliminate_zeros()

print(mat)

# Menghilangkan duplikat entri
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)
mat.sum_duplicates()

print(mat)

# Konversi dari csr ke csc
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

newarr = csr_matrix(arr).tocsc()

print(newarr)
"""
Catatan: Terlepas dari sparse specific operations yang disebutkan, sparse matrices mendukung semua operasi yang didukung oleh matriks normal, 
misalnya pembentukan ulang, penjumlahan, aritmatika, penyiaran, dll.
"""