print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.\n")

while True:
    try:
        item = int(input("Masukkan jumlah item: "))

        if item == 0:
            print("Toko ditutup. Sesi rekap selesai.")
            break

        if item < 0:
            print("Jumlah tidak boleh negatif")
            continue

        if item > 100:
            print("Maksimal 100 item per transaksi!")
            continue

        print(f"Transaksi {item} item berhasil!")

    except:
        print("Input harus berupa angka!")

