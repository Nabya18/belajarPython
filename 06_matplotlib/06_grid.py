"""
1. grid() fungsi untuk menambahkan garis kisi ke plot.
2. axis parameter dalam grid() fungsi untuk menentukan garis kisi mana yang akan ditampilkan.
    Nilainya adalah: 'x', 'y', dan 'both'. Nilai defaultnya adalah 'both'.
    x: hanya garis kisi vertikal.
    y: hanya garis kisi horizontal.
3. mengatur properti garis pada grid, seperti ini: grid(color = ' color ', linestyle = ' linestyle ', linewidth = number ).

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x', color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()