"""
Date Python
    Tanggal di Python bukanlah tipe datanya sendiri, tapi kita bisa mengimpor modul yang diberi nama datetimeagar berfungsi dengan tanggal sebagai objek tanggal.

1. Date Output
    a. Ketika kita mengeksekusi kode dari contoh di atas, hasilnya adalah:
        2024-03-28 01:57:06.393318
    b. Tanggal berisi tahun, bulan, hari, jam, menit, detik, dan mikrodetik.
    c. Modul ini datetime memiliki banyak metode untuk mengembalikan informasi tentang objek tanggal.

2. Membuat Objek Tanggal
    a. Untuk membuat tanggal, kita bisa menggunakan datetime()kelas (konstruktor) modul datetime.
    b. Kelas datetime() memerlukan tiga parameter untuk membuat tanggal: tahun, bulan, hari.
    c. Kelas datetime() juga mengambil parameter untuk waktu dan zona waktu (jam, menit, detik, mikrodetik, tzone), namun bersifat opsional, dan memiliki nilai default 0, (None untuk zona waktu).

3. Metode strftime()
    a. Objek tersebut datetime memiliki metode untuk memformat objek tanggal menjadi string yang dapat dibaca.
    b. Metode ini disebut strftime (), dan mengambil satu parameter, format, untuk menentukan format string yang dikembalikan

Referensi semua kode format hukum:
Directive	    Description	                                                        Example
%a	            Weekday, short version	                                            Wed
%A	            Weekday, full version	                                            Wednesday
%w	            Weekday as a number 0-6, 0 is Sunday	                            3
%d	            Day of month 01-31	                                                31
%b	            Month name, short version	                                        Dec
%B	            Month name, full version	                                        December
%m	            Month as a number 01-12	                                            12
%y	            Year, short version, without century	                            18
%Y	            Year, full version	                                                2018
%H	            Hour 00-23	                                                        17
%I	            Hour 00-12	                                                        05
%p	            AM/PM	                                                            PM
%M	            Minute 00-59	                                                    41
%S	            Second 00-59	                                                    08
%f	            Microsecond 000000-999999	                                        548513
%z	            UTC offset	                                                        +0100
%Z	            Timezone	                                                        CST
%j	            Day number of year 001-366	                                        365
%U	            Week number of year, Sunday as the first day of week, 00-53	        52
%W	            Week number of year, Monday as the first day of week, 00-53	        52
%c	            Local version of date and time	                                    Mon Dec 31 17:41:00 2018
%C	            Century	                                                            20
%x	            Local version of date	                                            12/31/18
%X	            Local version of time	                                            17:41:00
%%	            A % character	                                                    %
%G	            ISO 8601 year	                                                    2018
%u	            ISO 8601 weekday (1-7)	                                            1
%V	            ISO 8601 weeknumber (01-53)	                                        01
"""
# contoh => Impor modul datetime dan tampilkan tanggal saat ini
import datetime

x = datetime.datetime.now()
print(x)

# contoh => Kembalikan tahun dan nama hari kerja
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Contoh => Tampilkan nama bulan
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))