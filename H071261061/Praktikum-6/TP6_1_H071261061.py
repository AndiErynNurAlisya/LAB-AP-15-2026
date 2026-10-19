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
    hasil = [buku for buku in inventaris if kata_kunci.lower() in buku["judul"].lower()]
    print(f"Ditemukan {len(hasil)} buku:")
    for i, buku in enumerate(hasil, 1):
        print(f"{i}. {buku['judul']}")
        print(f"{buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")

def update_stok(inventaris, judul, jumlah):
    ditemukan = False
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            ditemukan = True
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print("Gagal! Stok menjadi negatif setelah perubahan.")
            else:
                buku["stok"] = stok_baru
                aksi = "berkurang" if jumlah < 0 else "bertambah"
                print(f"Stok '{buku['judul']}' {aksi} {abs(jumlah)}. Stok sekarang: {buku['stok']}")
            break
    if not ditemukan:
        print("Error: Buku tidak ditemukan!")

def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_nilai_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)
    
    if inventaris:
        buku_termahal = inventaris[0]
        for buku in inventaris:
            if buku["harga"] > buku_termahal["harga"]:
                buku_termahal = buku
        
        teks_termahal = f"{buku_termahal['judul']} (Rp{buku_termahal['harga']})"
    else:
        teks_termahal = "Tidak ada buku"

    print("========================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    print(f"Jumlah jenis buku: {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print("========================================")
    print(f"Total nilai aset : Rp{total_nilai_aset}")
    print(f"Buku termahal    : {teks_termahal}")
    print("========================================")


inventaris = []
while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
        
    pilihan = input("Pilih menu (1-5): ")
        
    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        try:
            harga = float(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif!")
                continue
            tambah_buku(inventaris, judul, penulis, harga, stok)
        except ValueError:
            print("Error: Harga harus berupa angka dan stok harus berupa bilangan bulat!")
        
    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)
            
    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Error: Jumlah perubahan harus berupa angka!")
                
    elif pilihan == "4":
        ringkasan_inventaris(inventaris)
            
    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break
    else:
        print("Pilihan tidak valid, silakan pilih antara 1-5.")

