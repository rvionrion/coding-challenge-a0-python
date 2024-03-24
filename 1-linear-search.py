"""
LINEAR SEARCH

Diberikan sebuah array yang berisi 10 nilai integer. Buat sebuah program yang dapat mencari nilai tertentu didalam array dengan menggunakan algoritma Linear Search. Tampilkan semua index dari nilai yang ditemukan. Apabila nilai yang dicari tidak ada didalam array maka tampilkan "Nilai {nilai_yang_dicari} tidak ditemukan".

Array = 40, 23, 17, 9, 40, 61, 23, 11, 40, 54

*Contoh Input*
Nilai yang dicari: 23

*Contoh Output*
Nilai 23 berada pada index-1
Nilai 23 berada pada index-6
"""

array = [40, 23, 17, 9, 40, 61, 23, 11, 40, 54]
nilai = int(input("Masukkan Nilai yang ingin dicari: "))

index_s = 0
index_f = len(array) - 1

nilai_ditemukan = False

while index_s <= index_f:
  if nilai == array[index_s]:
    nilai_ditemukan = True
    print(f"Nilai {nilai} berada pada index-{index_s}")

  index_s += 1

if nilai_ditemukan == False:
  print(f"Nilai {nilai} tidak ditemukan")
