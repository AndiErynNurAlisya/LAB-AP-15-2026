def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }

    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    hasil = []

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)

    if len(hasil) == 0:
        print("Buku tidak ditemukan.")
    else:
        print(f"Ditemukan {len(hasil)} buku:")
        for i, buku in enumerate(hasil, start=1):
            print(
                f"{i}. {buku['judul']} - {buku['penulis']} "
                f"| Rp{buku['harga']} | Stok: {buku['stok']}"
            )


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal! Stok tidak boleh negatif.")
            else:
                buku["stok"] = stok_baru

                if jumlah >= 0:
                    print(
                        f"Stok '{buku['judul']}' bertambah {jumlah}. "
                        f"Stok sekarang: {buku['stok']}"
                    )
                else:
                    print(
                        f"Stok '{buku['judul']}' berkurang {-jumlah}. "
                        f"Stok sekarang: {buku['stok']}"
                    )
            return

    print(f"Buku '{judul}' tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    print("=" * 39)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 39)


    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0
    buku_termahal = None

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]

        if buku_termahal is None:
            buku_termahal = buku
        elif buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku

    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")

    if buku_termahal is not None:
        print(
            f"Buku termahal     : {buku_termahal['judul']} "
            f"(Rp{buku_termahal['harga']})"
        )
    else:
        print("Buku termahal     : Belum ada buku")

    print("=" * 39)


def input_angka(pesan, minimal=0):
    while True:
        try:
            angka = int(input(pesan))

            if angka < minimal:
                print(f"Angka tidak boleh kurang dari {minimal}.")
            else:
                return angka

        except ValueError:
            print("Input harus berupa angka bulat!")


def program_utama():
    inventaris = []

    print("=" * 39)
    print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("=" * 39)

    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            judul = input("Judul buku: ").strip()
            penulis = input("Penulis: ").strip()

            if judul == "" or penulis == "":
                print("Judul dan penulis tidak boleh kosong.")
                continue

            harga = input_angka("Harga: ")
            stok = input_angka("Stok awal: ")

            tambah_buku(inventaris, judul, penulis, harga, stok)

        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ").strip()
            cari_buku(inventaris, kata_kunci)

        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ").strip()

            try:
                jumlah = int(
                    input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
                )
                update_stok(inventaris, judul, jumlah)

            except ValueError:
                print("Input jumlah harus berupa angka bulat!")

        elif pilihan == "4":
            ringkasan_inventaris(inventaris)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-5.")


program_utama()
