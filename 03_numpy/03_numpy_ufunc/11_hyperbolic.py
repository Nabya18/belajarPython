"""
NumPy Hyperbolic Functions
    NumPy menyediakan ufuncs sinh(), cosh()dan tanh()mengambil nilai dalam radian dan menghasilkan nilai sinh, cosh, dan tanh yang sesuai.

Menemukan Sudut
    Mencari sudut dari nilai sinh, cosh, tanh. Misal invers sinh, cosh dan tanh (arsinh, arcosh, artanh).
    NumPy menyediakan ufuncs arcsinh(), arccosh()dan arctanh()itu menghasilkan nilai radian untuk nilai sinh, cosh, dan tanh terkait yang diberikan.
"""
# Fungsi Hiperbolik
import numpy as np

x = np.sinh(np.pi/2)

print(x)

# Temukan nilai cosh untuk semua nilai di arr
import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.cosh(arr)

print(x)

## Menemukan Sudut
# Temukan sudut 1,0
import numpy as np

x = np.arcsinh(1.0)

print(x)

# Temukan sudut untuk semua nilai tanh dalam array
import numpy as np

arr = np.array([0.1, 0.2, 0.5])

x = np.arctanh(arr)

print(x)