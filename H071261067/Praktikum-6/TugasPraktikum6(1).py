#Tugas 1
inventaris_toko = []

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku_baru = {
        "judul": judul,
        "penulis": penulis,
        "harga" : harga,
        "stok": stok
    }
    inventaris.append(buku_baru)
    print(f"\nBuku {judul} berhasil ditambahkan ")
    print()

def cari_buku(inventaris, kata_kunci):
    hasil_cari = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil_cari.append(buku)
            
    if len(hasil_cari) > 0:
        print(f"Ditemukan {len(hasil_cari)} buku:")
    
        for i, buku in enumerate(hasil_cari, 1):
            print(f"  {i}. {buku['judul']} - {buku['penulis']} | {buku['harga']} | Stok: {buku['stok']}")
        print() 
    else:
        print("Buku tidak ditemukan.\n")

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0 :
                print("\nGagal! Stok tidak boleh kurang dari 0.")
                return

            buku["stok"] = stok_baru
            if jumlah > 0:
                print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {stok_baru}\n")
            elif jumlah < 0:
                print(f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {stok_baru}\n")
            else:
                print(f"Stok tidak berubah. Stok sekarang: {stok_baru}\n")
            return
            
    print("Judul buku tidak ditemukan.\n")

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("\nInventaris masih kosong")

    jumlah_jenis_buku = len(inventaris)
    total_stok  = 0
    total_aset = 0
    buku_termahal = inventaris[0]

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += (buku["harga"] * buku["stok"])

        if buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku

    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"Jumlah : {jumlah_jenis_buku}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset: {total_aset}")
    print(f"Buku termahal: {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print("=" * 40)

judul_sistem = "SISTEM INVENTARIS TOKO BUKU BOOKNEST"
panjang_border = 50 

print("=" * panjang_border)
print(judul_sistem.center(panjang_border))
print("=" * panjang_border)
print()
    
while True:
    print("Menu: ")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("\n-- Tambah Buku --")
        judul = input("Judul Buku: ")
        penulis = input("Penulis: ")

        try:
            harga = int(input("Harga (Rp): "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Error: Harga stok tidak boleh negatif")
            else:
                tambah_buku(inventaris_toko, judul, penulis, harga, stok)
        except ValueError:
            print("Error: Harga dan Stok harus berupa angka/digit")

    elif pilihan == "2":
        kata_kunci = input("\nMasukkan kata kunci judul buku: ")
        cari_buku(inventaris_toko, kata_kunci)

    elif pilihan == "3":
        judul = input("\nMasukkan judul buku yang ingin diupdate: ")
        try:
            perubahan = int(input("Jumlah perubahan (gunakan minus untuk mengurangi, misal -5): "))
            update_stok(inventaris_toko, judul, perubahan)
        except ValueError:
            print("Error: Jumlah perubahan harus berupa angka!")
            
    elif pilihan == "4":
        ringkasan_inventaris(inventaris_toko)
        
    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan sistem BookNest. Sampai jumpa!")
        break 
        
    else:
        print("\nPilihan tidak valid. Silakan masukkan angka 1-5.")
