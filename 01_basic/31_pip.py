"""
PIP adalah manajer package untuk package atau modul Python jika Kita mau.

Catatan: Jika Kita memiliki Python versi 3.4 atau lebih baru, PIP disertakan secara default.

Package
    1. Sebuah package berisi semua file yang Kita perlukan untuk sebuah modul.
    2. Modul adalah pustaka kode Python yang dapat Kita sertakan dalam proyek Kita.

1. pip --version => Periksa apakah PIP sudah terinstal
2. Instal PIP
    Jika Kita belum memasang PIP, Kita dapat mengunduh dan memasangnya dari halaman ini: https://pypi.org/project/pip/
3. Instal Package
    contoh: pip install camelcase
4. Menggunakan Package dengan import
    contoh: import camelcase
5. Temukan package => Temukan package lainnya di https://pypi.org/ .
6. Hapus package
    a. Gunakan uninstallperintah untuk menghapus package
        contoh: pip uninstall camelcase
    b. Manajer package PIP akan meminta Kita untuk mengonfirmasi bahwa Kita ingin menghapus package camelcase
7. Daftar package
    a. Gunakan listperintah untuk mencantumkan semua package yang diinstal pada sistem Kita
        contoh: pip list
"""

# Menggunakan package
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))