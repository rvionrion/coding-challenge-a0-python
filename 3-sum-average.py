"""
SUM & AVERAGE

Diberikan sebuah kumpulan bilangan bulat dalam bentuk array:

[ 7, 10, 5, 3, 5, 12, 1, 9, 18, 12 ]

Tulislah sebuah program yang dapat menghitung total (SUM) dan rata-rata (AVERAGE) dari nilai-nilai dalam array tersebut. Total adalah hasil penjumlahan semua nilai, sementara rata-rata adalah nilai rata-rata dari keseluruhan elemen array, dihitung dengan membagi total dengan jumlah elemen.

*Contoh output*
Total: 82
Rata-rata: 8.2
"""

data = [7, 10, 5, 3, 5, 12, 1, 9, 18, 12]
jumlah_elemen = len(data)
total = 0

index = 0

while index < jumlah_elemen:
  nilai = data[index]
  total += nilai
  index += 1

rata_rata = total / jumlah_elemen

print("Total:", total)
print("Rata-Rata:", rata_rata)
