"""
Nilai Rata-Rata

Nana adalah seorang mahasiswi yang ingin menghitung nilai rata-rata dari beberapa matakuliah yang dia ambil. Matakuliah tersebut adalah "Pemrograman Dasar", "Pemrograman Web" dan "Basis Data". Setiap matakuliah memiliki bobot sks (satuan kredit semester) yang berbeda. Berikut adalah bobot sks untuk setiap matakuliah :

Pemrograman Dasar : 2 sks
Pemrograman Web   : 3 sks
Basis Data        : 4 sks

Bantu Nana untuk membuat program yang dapat menghitung nilai rata-rata berdasarkan input nilai Nana untuk setiap matakuliah. 

Berikut contoh output yang dihasilkan :

=== Perhitungan Nilai Rata-Rata ===

Masukkan nilai Pemrograman Dasar : 85
Masukkan nilai Pemrograman Web : 78
Masukkan nilai Basis Data : 90

Nilai Rata-Rata : 84.88
"""

print("=== Perhitungan Nilai Rata-Rata ===")

nilai_pem_dasar = input("Masukkan nilai Pemrograman Dasar : ")
nilai_pem_dasar = int(nilai_pem_dasar) * 2

nilai_pem_web = input("Masukkan nilai Pemrograman Web : ")
nilai_pem_web = int(nilai_pem_web) * 3

nilai_basis_data = input("Masukkan nilai Basis Data : ")
nilai_basis_data = int(nilai_basis_data) * 4

total_nilai = nilai_pem_dasar + nilai_pem_web + nilai_basis_data
rata_rata = total_nilai / 9

print("")
print("Nilai Rata-Rata :", rata_rata)
