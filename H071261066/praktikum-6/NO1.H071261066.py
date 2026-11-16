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
    pencarian = []
    kata_kunci_lower = kata_kunci.lower()
    
    for buku in inventaris:
        if kata_kunci_lower in buku["judul"].lower():
            pencarian.append(buku)
            
    if pencarian:
        print(f"Ditemukan {len(pencarian)} buku:")
        for idx, b in enumerate(pencarian, 1):
            print(f"{idx}. {b['judul']} - {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")
    else:
        print("Buku tidak ditemukan.")

def update_stok(inventaris, judul, jumlah):
    buku_ditemukan = None
    for b in inventaris:
        if b["judul"].lower() == judul.lower():
            buku_ditemukan = b
            break
            
    if buku_ditemukan:
        stok_baru = buku_ditemukan["stok"] + jumlah
        if stok_baru < 0:
            print("Pesan gagal: Perubahan menyebabkan stok menjadi negatif.")
        else:
            buku_ditemukan["stok"] = stok_baru
            if jumlah >= 0:
                print(f"Stok '{buku_ditemukan['judul']}' bertambah {jumlah}. Stok sekarang: {stok_baru}")
            else:
                print(f"Stok '{buku_ditemukan['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {stok_baru}")
    else:
        print("Buku tidak ditemukan.")

def ringkasan_inventaris(inventaris):
    print("====================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("====================================")
    
    jumlah_jenis = len(inventaris)
    total_stok = sum(b["stok"] for b in inventaris)
    total_nilai = sum(b["harga"] * b["stok"] for b in inventaris)
    
    buku_termahal = ""
    if inventaris:
        termahal = max(inventaris, key=lambda x: x["harga"])
        buku_termahal = f"{termahal['judul']} (Rp{termahal['harga']})"
    else:
        buku_termahal = "-"

    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_nilai}")
    print(f"Buku termahal     : {buku_termahal}")

def main():
    inventaris_buku = []
    
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
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                
                if harga < 0 or stok < 0:
                    print("Pesan gagal: Harga dan stok tidak boleh negatif.")
                    continue
                    
                tambah_buku(inventaris_buku, judul, penulis, harga, stok)
            except ValueError:
                print("Pesan gagal: input harga dan stok berupa angka.")
                
        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris_buku, kata_kunci)
            
        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
                update_stok(inventaris_buku, judul, jumlah)
            except ValueError:
                print("Pesan gagal: input jumlah harus berupa angka.")
                
        elif pilihan == "4":
            ringkasan_inventaris(inventaris_buku)
            
        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break

if __name__ == "__main__":
    print("====================================")
    print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("====================================")
    main()