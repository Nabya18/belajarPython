"""
Array shape => jumlah elemen di setiap dimensi

Array NumPy memiliki atribut yang disebut shape yang mengembalikan tupel dengan setiap indeks memiliki jumlah elemen yang sesuai.

Apa yang diwakili oleh tupel shape
    1. Bilangan bulat pada setiap indeks menunjukkan jumlah elemen yang dimiliki dimensi terkait
    2. Pada contoh di bawah pada indeks-4 kita mempunyai nilai 4, sehingga kita dapat mengatakan bahwa dimensi ke-5 (4 + 1 th) mempunyai 4 elemen.
"""

# array 2-D
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

"""
Outputnya adalah (2, 4), yang berarti array ini memiliki 2 baris dan 4 kolom.
"""

# Buat array dengan 5 dimensi menggunakan ndmin vektor dengan nilai 1,2,3,4 dan verifikasi bahwa dimensi terakhir memiliki nilai 4
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

"""
Outputnya adalah [[[[[1 2 3 4]]]]], dan (1, 1, 1, 1, 4) yang berarti array ini memiliki 1 dimensi di setiap sumbu, dengan dimensi terakhir memiliki panjang 4.

Mengapa ini terjadi?
    Ketika Anda membuat array dengan ndmin=5, 
    Anda memaksa array itu memiliki setidaknya 5 dimensi, 
    yang berarti numpy akan menambahkan dimensi secara otomatis hingga mencapai 5 dimensi. 
    Namun, jumlah elemen dalam array Anda tetap sama. 
    Oleh karena itu, numpy menambahkan dimensi kosong (dengan panjang 1) untuk memenuhi syarat 5 dimensi yang Anda tentukan.

Jadi, mari kita bahas outputnya:
    [[[[[1 2 3 4]]]]]: Ini menunjukkan bahwa array tersebut memiliki 5 dimensi. 
    Jumlah kurung siku menunjukkan jumlah dimensi, dan elemen array terletak di dalam kurung siku terdalam.
    
    (1, 1, 1, 1, 4): Ini adalah bentuk dari array, yang menunjukkan panjang setiap dimensi dari array. 
    Angka terakhir adalah 4, menunjukkan bahwa dimensi terakhir memiliki panjang 4. 
    Yang lainnya adalah 1 karena numpy menambahkan dimensi kosong.
"""