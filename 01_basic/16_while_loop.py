"""
perulangan while => mengeksekusi sekumpulan pernyataan selama kondisinya benar.
1. Perulangan while memerlukan variabel yang relevan untuk disiapkan,
dalam contoh ini kita perlu mendefinisikan variabel pengindeksan, i , yang kita atur ke 1.
2. break => menghentikan perulangan meskipun kondisi while benar
3. continue => menghentikan iterasi saat ini, dan melanjutkan iterasi berikutnya
4. else => dapat menjalankan satu blok kode satu kali ketika kondisinya tidak lagi benar

"""

## contoh
# 1. Cetak i selama i kurang dari 6:
i = 1
while i < 6:
  print(i)
  i += 1    # jika tidak menambahkan i, perulangan akan berlanjut selamanya.

# contoh penggunaan break
i = 1
while i < 6:
  print(i)
  if i == 3: # hanya sampai 3
    break
  i += 1

# contoh continue
i = 0
while i < 6:
  i += 1
  if i == 3:  # 3 di skip
    continue
  print(i)

# contoh else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")