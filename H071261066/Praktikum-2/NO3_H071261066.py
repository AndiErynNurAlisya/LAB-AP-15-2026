nilai_tes = int(input("masukkan nilai tes anda: "))
pengalaman_kerja = int(input("masukkan pengalaman kerja anda(tahun): "))

if nilai_tes >= 80:
   status = "lolos ke tahap wawancara"
elif nilai_tes >= 65 and pengalaman_kerja >= 2:
   status = "lolos bersyarat"
else:
   status = "tidal lolos well"
print(status)
    
