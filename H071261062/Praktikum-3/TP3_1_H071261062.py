while True:
    try:
        # Meminta input dari kasir
        input_user = (input("Masukkan jumlah item: "))

        # Konversi input menjadi integer
        jumlah = int(input_user)

        # Kondisi 1: Menghentikan program jika input adalah 0
        if jumlah == 0:
            print("Toko ditutup. Sesi rekap selesai.")
            break

        # Kondisi 2: Angka negatif
        if jumlah < 0:
            print("Jumlah tidak boleh negatif")
            continue

        # Kondisi 3: Melebihi batas stok (lebih dari 100)
        if jumlah > 100:
            print("Maksimal 100 item per transaksi!")
            continue

        # Kondisi 4: Transaksi valid
        print(f"Transaksi {jumlah} item berhasil!")

    except ValueError:
        # Menangani error jika input bukan berupa angka bulat (huruf/simbol)
        print("Input harus berupa angka!")