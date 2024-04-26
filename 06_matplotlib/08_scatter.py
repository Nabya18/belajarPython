"""
scatter() fungsi tersebut untuk menggambar plot pencar.
    1. Fungsi ini scatter()memplot satu titik untuk setiap pengamatan.
    2. Dibutuhkan dua array dengan panjang yang sama, satu untuk nilai sumbu x, dan satu lagi untuk nilai pada sumbu y.

Warna
    Kita dapat mengatur warna Kita sendiri untuk setiap plot sebar dengan color atau c argumen

Warnai Setiap Titik
    mengatur warna tertentu untuk setiap titik dengan menggunakan serangkaian warna sebagai nilai argumen c.

Peta warna
    1. Modul Matplotlib memiliki sejumlah peta warna yang tersedia.
    2. Peta warna seperti daftar warna, di mana setiap warna memiliki nilai yang berkisar antara 0 hingga 100.
    3. Peta warna ini disebut 'viridis' dan seperti yang Kita lihat, peta warna ini berkisar dari 0, yaitu warna ungu, hingga 100, yaitu warna kuning.
    4. Cara Menggunakan Peta Warna;
        - Kita dapat menentukan peta warna dengan argumen kata kunci cmap dengan nilai peta warna,
        - dalam hal ini 'viridis'yang merupakan salah satu peta warna bawaan yang tersedia di Matplotlib.
        - Selain itu, Kita harus membuat array dengan nilai (dari 0 hingga 100), satu nilai untuk setiap titik di plot sebar
    5. Kita dapat menyertakan peta warna dalam gambar dengan menyertakan plt.colorbar() pernyataan
    6. Peta warna yang tersedia
        Name		 	        Reverse
        Accent		 	        Accent_r
        Blues		 	        Blues_r
        BrBG		 	        BrBG_r
        BuGn		 	        BuGn_r
        BuPu		 	        BuPu_r
        CMRmap		 	        CMRmap_r
        Dark2		 	        Dark2_r
        GnBu		 	        GnBu_r
        Greens		 	        Greens_r
        Greys		 	        Greys_r
        OrRd		 	        OrRd_r
        Oranges		 	        Oranges_r
        PRGn		 	        PRGn_r
        Paired		 	        Paired_r
        Pastel1		 	        Pastel1_r
        Pastel2		 	        Pastel2_r
        PiYG		 	        PiYG_r
        PuBu		 	        PuBu_r
        PuBuGn		 	        PuBuGn_r
        PuOr		 	        PuOr_r
        PuRd		 	        PuRd_r
        Purples		 	        Purples_r
        RdBu		 	        RdBu_r
        RdGy		 	        RdGy_r
        RdPu		 	        RdPu_r
        RdYlBu		 	        RdYlBu_r
        RdYlGn		 	        RdYlGn_r
        Reds		 	        Reds_r
        Set1		 	        Set1_r
        Set2		 	        Set2_r
        Set3		 	        Set3_r
        Spectral		        Spectral_r
        Wistia		 	        Wistia_r
        YlGn		 	        YlGn_r
        YlGnBu		 	        YlGnBu_r
        YlOrBr		 	        YlOrBr_r
        YlOrRd		 	        YlOrRd_r
        afmhot		 	        afmhot_r
        autumn		 	        autumn_r
        binary		 	        binary_r
        bone		 	        bone_r
        brg		 	            brg_r
        bwr		 	            bwr_r
        cividis		 	        cividis_r
        cool		 	        cool_r
        coolwarm		        coolwarm_r
        copper		 	        copper_r
        cubehelix		        cubehelix_r
        flag		 	        flag_r
        gist_earth		 	    gist_earth_r
        gist_gray		 	    gist_gray_r
        gist_heat		 	    gist_heat_r
        gist_ncar		 	    gist_ncar_r
        gist_rainbow		 	gist_rainbow_r
        gist_stern		 	    gist_stern_r
        gist_yarg		 	    gist_yarg_r
        gnuplot		 	        gnuplot_r
        gnuplot2		 	    gnuplot2_r
        gray		 	        gray_r
        hot		 	            hot_r
        hsv		 	            hsv_r
        inferno		 	        inferno_r
        jet		 	            jet_r
        magma		 	        magma_r
        nipy_spectral		 	nipy_spectral_r
        ocean		 	        ocean_r
        pink		 	        pink_r
        plasma		 	        plasma_r
        prism		 	        prism_r
        rainbow		 	        rainbow_r
        seismic		 	        seismic_r
        spring		 	        spring_r
        summer		 	        summer_r
        tab10		 	        tab10_r
        tab20		 	        tab20_r
        tab20b		 	        tab20b_r
        tab20c		 	        tab20c_r
        terrain		 	        terrain_r
        twilight		 	    twilight_r
        twilight_shifted	    twilight_shifted_r
        viridis		 	        viridis_r
        winter		 	        winter_r

Ukuran
    1. Kita dapat mengubah ukuran titik dengan s argumen.
    2. Sama seperti warna, pastikan array untuk ukuran memiliki panjang yang sama dengan array untuk sumbu x dan y

Transparansi titik
    1. Kita dapat mengatur transparansi titik-titik dengan alphaargumen.
    2. Sama seperti warna, pastikan array untuk ukuran memiliki panjang yang sama dengan array untuk sumbu x dan y
"""
## scatter plot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
"""
Pengamatan pada contoh di atas merupakan hasil dari 13 mobil yang lewat.
    Sumbu X menunjukkan umur mobil.
    Sumbu Y menunjukkan kecepatan mobil saat melintas.

Berdasarkan data di atas, nampaknya semakin baru mobilnya maka semakin cepat pula melajunya.
"""

## Gambarlah dua plot pada gambar yang sama
import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.legend()
plt.show()

## atur warna pada plot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()

## atur warna pada setiap dot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()

## Buat array warna, dan tentukan peta warna di plot sebar
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()

## Tetapkan ukuran Kita sendiri untuk penanda
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()

## Tetapkan ukuran Kita sendiri untuk penanda
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

## Menggabungkan ukuran, warna, dan transparansi titik
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()