"""
1. Mean: nilai rata-rata, menggunakan Numpy mean()
2. Median: nilai titik tengah, menggunakan Numpy median()
3. Mode: nilai yang paling sering muncul, menggunakan Scipy stats.mode()
"""
# Mean
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

# Median
import numpy

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

# Mode
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)