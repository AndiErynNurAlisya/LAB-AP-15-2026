
tujuan = input("Masukkan Tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan Waktu (Pagi/Malam): ")
tipe_pengunjung = input("Masukkan Tipe Pengunjung (Anak/Dewasa): ")

rekomendasi = "Tidak ada paket yang cocok"

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            rekomendasi = "Paket A"
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            rekomendasi = "Paket C"

    case "Pegununungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            rekomendasi = "Paket B"
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            rekomendasi = "Paket C"

    case "Kota":
        if waktu == "Malam":
            rekomendasi = "Paket C"
print(f"Rekomendasi Paket: {rekomendasi}")