n_kursi = int(input("jumlah kursi bus (N): "))

total_pendapataan = 0
sisa_kursi = n_kursi

while sisa_kursi > 0:
    print(f"\nsisa kursi tersedia {sisa_kursi}")
    umur = int(input("msukkan umur anda: "))

    if umur < 0:
        print("umur tidak valid")
        continue

    if 0 <= umur <= 5:
        harga_tiket = 0
        print("kategori balita tiket gratis")
    elif  6 <= umur <= 12:
        harga_tiket = 50000
    else:
        harga_tiket = 100000

    sisa_kursi -= 1
    total_pendapataan += harga_tiket
    

print("\npesanan selesai")
print(f"seluru kursi {n_kursi} telah terisi")
print(f"semua pendapatan perjalanaan PO BUS kali ini adalah {total_pendapataan}")
