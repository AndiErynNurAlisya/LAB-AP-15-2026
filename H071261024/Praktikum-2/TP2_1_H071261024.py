cabai = float(input("Masukkan persentase cabai: "))

if 70 < cabai <= 100:
    print("Level Ekstrem")
elif 40 < cabai <= 70:
    print("Level Pedas")
elif 10 < cabai <= 40:
    print("Level Sedang")
elif 0 <= cabai <= 10:
    print("Level Aman")
else:
    print("Tidak Valid")