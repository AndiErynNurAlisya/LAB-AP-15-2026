def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip()

    if nama == "":
        return

    nama = nama.title()

    if nama in kandidat_set:
        print(f"Kandidat '{nama}' sudah terdaftar!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.strip().lower()
    pilihan = pilihan.strip().title()

    if pilihan not in kandidat_set:
        print(f"Kandidat '{pilihan}' tidak terdaftar. Suara tidak dicatat!")
        return

    if nama_pemilih in rekap_suara:
        print(f"'{nama_pemilih.title()}' sudah memberikan suara sebelumnya!")
        return

    rekap_suara[nama_pemilih] = pilihan
    print(f"Suara '{nama_pemilih.title()}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("\n======================================")
    print("     HASIL PEMILIHAN KETUA KELAS")
    print("======================================")

    if len(perolehan) == 0:
        print("Belum ada kandidat yang terdaftar.")
        print("Total suara masuk: 0")
        print("Belum ada pemenang.")
        print("======================================")
        return

    for kandidat in sorted(perolehan):
        print(f"  {kandidat}: {perolehan[kandidat]} suara")

    total_suara = sum(perolehan.values())
    suara_tertinggi = max(perolehan.values())

    pemenang = []

    for kandidat, jumlah in perolehan.items():
        if jumlah == suara_tertinggi:
            pemenang.append(kandidat)

    print(f"\nTotal suara masuk: {total_suara}")

    if len(pemenang) > 1:
        print("Hasil SERI antara: " + ", ".join(sorted(pemenang)))
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(
            f"PEMENANG: {pemenang[0]} "
            f"dengan {suara_tertinggi} suara!"
        )

    print("======================================")


def program_utama():
    kandidat_set = set()
    rekap_suara = {}

    print("======================================")
    print("     SISTEM PEMILIHAN KETUA KELAS")
    print("======================================")


    print("\n--- FASE PENDAFTARAN KANDIDAT ---")

    while True:
        nama = input(
            "Masukkan nama kandidat (kosongkan untuk selesai): "
        ).strip()

        if nama == "":
            break

        daftar_kandidat(kandidat_set, nama)

    if len(kandidat_set) < 2:
        print("Kandidat minimal harus 2 orang. Program dihentikan.")
        return

    print(f"\nKandidat terdaftar: {kandidat_set}")


    print("\n--- FASE PEMUNGUTAN SUARA ---")

    while True:
        nama_pemilih = input(
            "\nNama pemilih (kosongkan untuk selesai): "
        ).strip()

        if nama_pemilih == "":
            break

        print(f"Kandidat yang tersedia: {kandidat_set}")

        pilihan = input("Pilih kandidat: ").strip()

        if pilihan == "":
            print("Pilihan kandidat tidak boleh kosong.")
            continue

        berikan_suara(
            rekap_suara,
            kandidat_set,
            nama_pemilih,
            pilihan
        )

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)


program_utama()
