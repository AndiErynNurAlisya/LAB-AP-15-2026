while True:
    try:
        kursi = int(input("Masukkan maksimal kursi bus: "))
        if kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!\n")
            continue
        break

    except:
        print("Input jumlah kursi harus berupa angka!\n")

sisa_kursi = kursi
total_pendapatan = 0

print("\n--- Sistem Reservasi PO BUS Dimulai ---\n")

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")

    try:
        umur = int(input("Masukkan umur penumpang: "))
        if umur < 0:
            print("Umur tidak valid!\n")
            continue
    except:
        print("Input umur harus berupa angka!\n")   
        continue

    if 0 <= umur <= 5:
        harga = 0
        print("Kategori: Balita - Tiket Gratis (Rp 0)\n")
    elif 6 <= umur <= 12:
        harga = 50000
        print("Kategori: Anak - Harga: Rp 50.000\n")
    else:
        harga = 100000
        print("Kategori: Dewasa - Harga: Rp 100.000\n")

    sisa_kursi -= 1
    total_pendapatan += harga

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatam perjalanan PO BUS kali ini: Rp {total_pendapatan}")
