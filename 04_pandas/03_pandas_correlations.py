"""
Pandas - Data Correlations

Menemukan Hubungan
Aspek hebat dari modul Pandas adalah corr()m etodenya.
Metode ini corr() menghitung hubungan antara setiap kolom dalam kumpulan data Anda.
Catatan: Metode ini corr()mengabaikan kolom "bukan numerik".

Apa korelasi yang baik? Itu tergantung pada penggunaannya, tapi menurut saya aman untuk mengatakan Kita harus memiliki setidaknya 0.6(atau -0.6) untuk menyebutnya korelasi yang baik.
Ada beberapa alasan mengapa angka ini sering dijadikan patokan untuk korelasi yang baik:
    1. Kekuatan Hubungan: Angka 0.6 menunjukkan bahwa ada hubungan yang cukup kuat antara dua variabel. Ini berarti bahwa perubahan dalam satu variabel cenderung disertai dengan perubahan yang sebanding dalam variabel lainnya.
    2. Konsistensi: Nilai 0.6 menunjukkan bahwa hubungan antara variabel tersebut konsisten dan dapat diandalkan. Ini berarti bahwa pola hubungan tersebut dapat diamati secara teratur dalam data.
    3. Relevansi Praktis: Nilai 0.6 memberikan indikasi bahwa hubungan tersebut memiliki relevansi praktis atau signifikansi dalam konteks di mana data tersebut digunakan. Ini penting untuk mengambil keputusan atau membuat prediksi yang akurat.

Korelasi Sempurna:
Kita dapat melihat bahwa "Durasi" dan "Durasi" mendapat nomor 1.000000, yang masuk akal, setiap kolom selalu memiliki hubungan yang sempurna dengan dirinya sendiri.

Korelasi yang Baik:
"Durasi" dan "Kalori" mempunyai 0.922721 korelasi yang merupakan korelasi yang sangat baik, dan kita dapat memperkirakan bahwa semakin lama Kita berolahraga, semakin banyak kalori yang Kita bakar, dan sebaliknya: jika Kita membakar banyak kalori, Kita mungkin sudah lama berolahraga.

Korelasi Buruk:
“Duration” dan “Maxpulse” mempunyai 0.009403 korelasi yang merupakan korelasi yang sangat buruk, artinya kita tidak bisa memprediksi max pulse hanya dengan melihat durasi latihan, begitu pula sebaliknya.
"""
# Tunjukkan hubungan antar kolom
import pandas as pd
df = pd.read_csv('data.csv')
print(df.corr())
"""
Hasil dari corr()metode ini adalah tabel dengan banyak angka yang mewakili seberapa baik hubungan antara dua kolom.
Angkanya bervariasi dari -1 hingga 1.
    1 berarti terdapat hubungan 1 banding 1 (korelasi sempurna), dan untuk kumpulan data ini, setiap kali nilai pada kolom pertama naik, nilai yang lain juga ikut naik.
    0,9 juga merupakan hubungan yang baik, dan jika Kita meningkatkan satu nilai, kemungkinan besar nilai lainnya juga akan meningkat.
    -0,9 akan menjadi hubungan yang sama baiknya dengan 0,9, namun jika Kita meningkatkan satu nilai, nilai lainnya mungkin akan turun.
    0,2 artinya BUKAN hubungan yang baik, artinya jika nilai yang satu naik belum tentu nilai yang lain naik.
"""