"""
WAKTU KEBERANGKATAN SISWA

Buatlah sebuah program untuk menentukan waktu keberangkatan siswa ke sekolah berdasarkan jarak rumah, dengan ketentuan sebagai berikut:

a. JIKA jarak rumah kurang dari 5 KM, maka siswa harus berangkat pukul 06.15

b. sebaliknya, JIKA jarak lebih dari 5 KM, maka siswa harus berangkat pukul 05.45.

Program menggunakan tipe data integer, variable yang digunakan 1. Gunakan IF 2 kondisi (IF-THEN-ELSE ).
"""

jarak_rumah = int(input("Masukkan Jarak Rumah (KM): "))

if jarak_rumah < 5:
  print("Siswa harus berangkat pukul 06.15")
else:
  print("Siswa harus berangkat pukul 05.45")
