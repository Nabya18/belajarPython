"""
Hapus File
1. Untuk menghapus file, Kita harus mengimpor modul OS, dan menjalankan fungsinya os.remove():
2. Untuk menghapus seluruh folder, gunakan os.rmdir() metode
contoh: Hapus folder "folder saya":
    import os
    os.rmdir("myfolder")

Catatan: Kita hanya dapat menghapus folder kosong .
"""

# Hapus file "demofile.txt"
# import os
# os.remove("demofile.txt")

# Periksa apakah file ada, lalu hapus:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")