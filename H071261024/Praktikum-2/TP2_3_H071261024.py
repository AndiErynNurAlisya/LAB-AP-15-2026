tes_tertulis = float(input("Masukkan nilai tes: "))
pengalaman = float(input("Masukkan pengalam kerja (tahun): "))

if tes_tertulis >= 80:
    print("Lolos ke Tahap Wawancara")
elif 65 <= tes_tertulis < 80 and pengalaman >= 2:
    print("Lolos Bersyarat")
else:
    print("Tidak Lolos")