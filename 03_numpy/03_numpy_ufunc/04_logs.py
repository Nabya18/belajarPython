"""
Log
    1. NumPy menyediakan fungsi untuk melakukan log pada basis 2, e dan 10
    2. Kami juga akan mengeksplorasi bagaimana kami dapat mengambil log untuk basis apa pun dengan membuat ufunc khusus.
    3. Semua fungsi log akan menempatkan -inf atau inf dalam elemen jika log tidak dapat dihitung.

1. Log at Base 2 => Gunakan log2() fungsi untuk melakukan log di basis 2.
2. Log at Base 10 => Gunakan log10() fungsi untuk melakukan log di basis 10.
3. Natural Log, atau Log at Base e => Gunakan log()fungsi untuk melakukan log di pangkalan e.
4. Log at Any Base
    - NumPy tidak menyediakan fungsi apa pun untuk mengambil log di basis mana pun,
    - jadi kita dapat menggunakan frompyfunc() fungsi tersebut bersama dengan fungsi bawaan math.log() dengan dua parameter masukan dan satu parameter keluaran
"""
# Log at Base 2
import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))

"""
Kode yang Kita berikan menggunakan pustaka NumPy di Python untuk membuat larik dari 1 hingga 9 dengan np.arange(1, 10), 
yang menghasilkan larik [1, 2, 3, 4, 5, 6, 7, 8, 9].

Kemudian, Kita menggunakan fungsi np.log2() dari NumPy untuk menghitung logaritma basis 2 dari setiap elemen dalam larik tersebut.

Jadi, output dari np.log2(arr) akan menjadi:
    1. Logaritma basis 2 dari 1 adalah 0
    2. Logaritma basis 2 dari 2 adalah 1
    3. Logaritma basis 2 dari 3 akan mendekati 1.5849625
    4. Dan seterusnya.

Output dari kode ini akan menjadi nilai-nilai logaritma basis 2 dari setiap elemen dalam larik [1, 2, 3, 4, 5, 6, 7, 8, 9].
"""

# Log at Base 10
import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))

# Natural Log, or Log at Base e
import numpy as np

arr = np.arange(1, 10)

print(np.log(arr))

"""
Output berbeda karena kedua fungsi logaritma (np.log10() dan np.log()) 
menggunakan basis yang berbeda untuk menghitung logaritma dari setiap elemen dalam larik.
    1. np.log10() menghitung logaritma basis 10, sedangkan
    2. np.log() menghitung logaritma basis e atau logaritma natural.
"""

# Log at Any Base
from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(200, 15))

"""
Fungsi np.frompyfunc mengonversi fungsi Python biasa menjadi fungsi Universal NumPy, 
yang memungkinkan Kita menerapkannya pada array NumPy secara efisien. 
Dalam kasus ini, Kita mengonversi fungsi logaritma standar Python menjadi fungsi Universal NumPy.

Namun, fungsi logaritma dalam panggilan Kita adalah logaritma dengan basis alami (logaritma natural), 
yang berbeda dari logaritma basis 10 yang mungkin diharapkan. 
Jadi, hasilnya adalah logaritma natural dari 100 basis 15, yang diperkirakan sebesar 1.7005483074552052.

hasilnya sama dengan print(np.log10(100) / np.log10(15)), 
yang menghitung logaritma basis 10 dari 100 dan 15, dan kemudian membagi hasilnya.
"""