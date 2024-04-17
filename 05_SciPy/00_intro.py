"""
1. SciPy adalah perpustakaan komputasi ilmiah yang menggunakan NumPy di bawahnya.
2. Ini menyediakan lebih banyak fungsi utilitas untuk optimasi, statistik dan pemrosesan sinyal.
3. SciPy telah mengoptimalkan dan menambahkan fungsi yang sering digunakan di NumPy dan Ilmu Data.
4. SciPy dibuat oleh pencipta NumPy, Travis Olliphant.
"""

# Berapa meter kubik dalam satu liter
from scipy import constants

print(constants.liter)
"""
constants = SciPy menawarkan sekumpulan konstanta matematika, salah satunya adalah litermengembalikan 1 liter sebagai meter kubik.
"""

# Memeriksa Versi SciPy
import scipy

print(scipy.__version__)