while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))
        print("\n")
        if N < 0:
            print("Maksimal kursi tidak boled < 0!")
            continue

        break

    except:
        print("Input jumlah kursi harus berupa angka!")

print("--- Sistem Reservasi PO BUS Dimulai ---\n")
total = 0
while N > 0:
    try:
        print("Sisa kursi: ",N)
        M = int(input("Masukkan umur penumpang: "))
        if M < 0 :
            print("Umur tidak valid!\n")
            continue
    

        elif 0 <= M <= 5:
            N -= 1
            print("Kategori: Balita - Tiket Gratis (Rp 0)\n")

        elif 6 <= M <= 12:
            N -= 1
            total += 50000
            print("Kategori: Anak - Harga: Rp 50.000\n")

        elif M > 12:
            N -= 1
            total += 100000
            print("Kategori: Dewasa - Harga: Rp 100.000\n")

    except:
        print("Input harus berupa angka!\n")
        continue

print("--- Semua Kursi Terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini: ",total)

    
