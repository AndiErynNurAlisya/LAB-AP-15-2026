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
    kata_kunci_low = kata_kunci.lower()
    hasil = []

    for buku in inventaris:
        judul_low = buku["judul"].lower()
        if kata_kunci_low in judul_low:
            hasil.append(buku)

    if hasil:
        print(f"Ditemukan {len(hasil)} buku:")
        nomor = 1
        for buku in hasil:
            print(f"   {nomor}. {buku['judul']} - {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")
            nomor += 1
    else:
        print("Buku tidak ditemukan!")

def update_stok(inventaris, judul, jumlah):
    ditemukan = False

    for buku in inventaris:
        if buku["judul"].lower()==judul.lower():
            ditemukan = True
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal! Stok menjadi negatif.")
            else:
                buku["stok"] = stok_baru
                if jumlah >= 0:
                    print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {buku['stok']}")
                else:
                    print(f"Stok '{buku['judul']}' berkurang {-jumlah}. Stok sekarang: {buku['stok']}")
            break

    if not ditemukan:
        print("Error: Buku tidak ditemukan.")

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris masih kosong!")
        return

    jumlah_jenis_buku = len(inventaris)
    total_seluruh_stok = 0
    total_nilai_aset = 0
    buku_termahal = inventaris[0]

    for buku in inventaris:
        total_seluruh_stok += buku["stok"]
        nilai_aset = buku["stok"] * buku["harga"]
        total_nilai_aset += nilai_aset

        if buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku

    garis = "=" * 50
    print(garis)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print(garis)
    print(f"Jumlah jenis buku  : {jumlah_jenis_buku}")
    print(f"Total seluruh stok : {total_seluruh_stok}")
    print(f"Total nilai aset   : Rp{total_nilai_aset}")
    print(f"Buku termahal      : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print(garis)

inventaris = []

garis = "=" * 40
print(garis)
print("  SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print(garis)

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        try:
            harga = float(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh kurang dari 0 (negatif)!")
                continue
            tambah_buku(inventaris, judul, penulis, harga, stok)
        except ValueError:
            print("Error: Harga harus berupa angka dan stok berupa angka bulat! ")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Error: Jumlah harus berupa angka bulat!")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid, harus berupa angka (1-5)!")

