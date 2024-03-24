"""
VALIDASI WAKTU

Buatlah program yang akan meminta user memasukkan 3 angka yang dipisahkan dengan tanda titik dua ":", seperti 07:15:15, angka-angka ini adalah jam:menit:detik. Program akan memeriksa apakah jam, menit, detik yang diperiksa valid atau tidak ( dalam format 24 jam ).

Contoh:
 13:13:13 ( Valid )
 25:01:01 ( Tidak Valid )
"""

waktu = input("Masukkan Waktu (jam:menit:detik) : ")
waktu = waktu.split(":")

if len(waktu) != 3:
  print("tidak valid")

else:
  jam = int(waktu[0])
  menit = int(waktu[1])
  detik = int(waktu[2])

  waktu_valid = False

  # jam 0 - 23 | menit 0 - 59 | detik 0 - 59
  if (jam <= 23 and jam >= 0) and (menit <= 59 and menit >= 0) and (detik <= 59 and detik >= 0):
    waktu_valid = True

  if waktu_valid:
    print("valid")
  else:
    print("tidak valid")
