#Tugas Praktikum 3
nilai_tes = int(input("Masukkan nilai tes: "))
pengalaman_kerja = int(input("Masukkan pengalaman kerja anda (tahun): "))

#Hasil Kualifikasi
if nilai_tes >= 80:
    print("Lolos Ke Tahap Wawancara")
elif nilai_tes < 80 and nilai_tes >= 60 and pengalaman_kerja >= 2:
    print("Lolos Bersyarat")
else :
 print("Tidak Lolos")
