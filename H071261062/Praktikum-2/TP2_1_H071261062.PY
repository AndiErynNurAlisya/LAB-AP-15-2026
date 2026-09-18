kepedasan = int(input("Masukkan presentase cabai : "))

if kepedasan >= 0 and kepedasan <= 10:
    print("Level Aman")
elif kepedasan >= 11 and kepedasan <= 40:
    print("Level Sedang")
elif kepedasan >= 41 and kepedasan <= 70:
    print("Level Pedas")
elif kepedasan >= 70 and kepedasan <= 100:
    print("Level Ekstrem")
else:
    print("Invalid")
    
