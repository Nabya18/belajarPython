"""
Random permutation => Permutasi mengacu pada susunan elemen. misal [3, 2, 1] merupakan permutasi dari [1, 2, 3] dan sebaliknya.
    1. shuffle()        : mengubah susunan elemen pada tempatnya. yaitu membuat perubahan pada array asli.
    2. permutation()    : mengembalikan array yang disusun ulang (dan membiarkan array asli tidak berubah).
"""
# shuffle()
from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)


# permutation()
arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))