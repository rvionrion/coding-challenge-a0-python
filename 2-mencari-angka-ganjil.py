"""
MENCARI ANGKA GANJIL

Buat program yang menerima inputan bilangan bulat positif (N), dengan batasan maksimal adalah N = 50. Program harus menghasilkan deretan angka dari 1 sampai N, dan mengganti semua angka ganjil dalam deretan tersebut dengan kata "ganjil".

Batasan Nilai (N) :
- Nilai N harus merupakan bilangan bulat positif.
- Nilai N tidak boleh melebihi 50.

Input:
Satu angka (N). Dimana (N) merupakan bilangan bulat positif ( maksimum 50 ).

Output:
Deretan angka dari 1 sampai (N). Semua angka ganjil diubah menjadi kata "ganjil".

Test Cases :
-------------------------------------------------------------------------
Input                Output
-------------------------------------------------------------------------
5                    ganjil 2 ganjil 4 ganjil
10                   ganjil 2 ganjil 4 ganjil 6 ganjil 8 ganjil 10
51                   Nilai maksimal yang diinputkan adalah 50
"""

bilangan_n = int(input("Masukkan Bilangan : "))
angka = 1

if bilangan_n > 50:
  print("Nilai maksimal yang diinputkan adalah 50")
else:
  while angka <= bilangan_n:
    if angka % 2 == 1:
      print("ganjil", end=" ")
    else:
      print(angka, end=" ")
    angka += 1
