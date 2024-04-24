"""
1. Fungsi xlabel() dan ylabel() untuk menyetel label pada sumbu x dan y.
2. title() fungsi tersebut untuk menetapkan judul plot
3. fontdict parameter di xlabel(), ylabel(), dan title() untuk mengatur properti font untuk judul dan label.
4. loc parameter in title()untuk memposisikan judul.
    Nilainya adalah: 'left', 'right', and 'center'. Nilai defaultnya adalah 'center'.
5. color parameter in title() untuk mengatur warna judul.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1, loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()