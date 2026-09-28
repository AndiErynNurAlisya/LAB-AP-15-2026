print("dins store")
while True:
    input_kuu = input("masukkan jumlah item: ")

    try:
        jumlah = int(input_kuu)
    except ValueError:
        print("input harus berupa angka!")
        continue

    if jumlah < 0:
        print("jumlah tidak boleh negatif")
        continue

    if jumlah > 100:
        print("maksimal 100 item pertransaksi")
        continue

    if jumlah == 0:
        print("toko ditutup, sesi rekap selesai")
        break

    else:
        print(f"transaksi [{jumlah}] item telah berhasil")