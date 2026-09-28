#no.3
nilai = int(input("masukkan nilai tes : "))

if nilai >= 80 :
    print("Lolos ke Tahap Wawancara")
elif 65 <= nilai < 80:
    pengalaman = int(input("masukkan pengalaman kerja (tahun) : "))
    if pengalaman >= 2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")
else:
    print("Tidak Lolos")