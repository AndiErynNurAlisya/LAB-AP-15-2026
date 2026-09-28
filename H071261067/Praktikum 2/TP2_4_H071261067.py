#Tugas Praktikum 4
tujuan = input("Masukkan Tujuan Anda (Pantai/pegunungan/Kota): ")
waktu = input("Masukkan Waktu Anda (Pagi/Malam): ")
tipe_pengunjung =  input("Masukkan Tipe Pengunjung(Anak/Dewasa): ")

#Kondisi
match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print("Paket Rekomendasi : Paket A")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print("Paket Rekomendasi : Paket C")
        else: print("Tidak ada paket yang cocok")
    case "Pegunungan":
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa":
            print("Paket Rekomendasi : Paket B")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            print("Paket Rekomendasi : Paket C")
        else: print("Tidak ada paket yang cocok")
    case "Kota":
        if waktu == "Malam":
            print("Paket Rekomendasi : Paket C")
        else: print("Tidak ada paket yang cocok")
