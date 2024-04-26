"""
Membuat Diagram Lingkaran
    pie() fungsi untuk menggambar diagram lingkaran.

Label
    1. Tambahkan label ke diagram lingkaran dengan labels parameter.
    2. Parameternya labelsharus berupa array dengan satu label untuk setiap irisan.

Start Angle
    1. Seperti disebutkan, sudut awal default adalah pada sumbu x, tetapi Kita dapat mengubah sudut awal dengan menentukan startangle parameter.
    2. Parameter startangleditentukan dengan sudut dalam derajat, sudut default adalah 0

Explode
    1. Parameter explode memungkinkan agar salah satu wedgesnya menonjol
    2. Parameternya explode, jika ditentukan, dan bukan None, harus berupa array dengan satu nilai untuk setiap irisan.

Shadow
    1. Tambahkan bayangan ke diagram lingkaran dengan shadow parameter = True.
    2. Parameter shadow adalah opsional dan defaultnya adalah False.

Warna
    1. Kita dapat mengatur warna setiap irisan dengan colorsparameternya.
    2. Parameternya colors, jika ditentukan, harus berupa array dengan satu nilai untuk setiap irisan

Legend
    Untuk menambahkan daftar penjelasan pada setiap irisan, gunakan fungsi legend()

Legend Dengan Header
    Untuk menambahkan header ke legenda, tambahkan title parameter ke legend fungsi.
"""
## Diagram lingkaran sederhana
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

## Diagram lingkaran sederhana
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()

## Mulai irisan pertama pada 90 derajat
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

## arik irisan "Apel" 0,2 dari tengah pai
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()

## Tambahkan bayangan
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()

## Tentukan warna baru untuk setiap irisan
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

## Tambahkan legend
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()

## Tambahkan legenda dengan header
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()