tes = int(input("masukkan nilai tes : "))

if tes >= 80 :
    print("Lolos Ke Tahap Wawancara")
elif tes >= 65 and tes <= 80:
    pengalaman = int(input("masukkan pengalaman kerja (Tahun) : "))
    if pengalaman >= 2:
        print("Loloss Bersyarat")
else: 
    print("tidak lolos")