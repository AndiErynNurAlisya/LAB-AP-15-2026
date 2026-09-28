#no.4
tujuan = input("Masukkan Tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan Waktu (Pagi/Malam): ")
tipe_pengunjung = input("Masukkan Tipe Pengunjung (Anak/Dewasa): ")

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print("Paket A")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case "Pegunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            print("Paket B")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case "Kota":
        if waktu == "Malam":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case _:
        print("Tidak ada paket yang cocok")
