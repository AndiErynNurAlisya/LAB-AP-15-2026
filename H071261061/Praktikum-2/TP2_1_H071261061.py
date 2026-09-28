#no 1.
tingkat_kepedasan = int(input("Tingkat Kepedasan : "))

if 0 <= tingkat_kepedasan <= 10:
    print("Level Aman")
elif 11 <= tingkat_kepedasan <= 40:
    print("Level Sedang")
elif 41 <= tingkat_kepedasan <= 70:
    print("Level Pedas")
elif tingkat_kepedasan > 70:
    print("Level Ekstrem")
else:
    print("tidak valid")
