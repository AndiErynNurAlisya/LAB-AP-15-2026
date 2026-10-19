def format_durasi(durasi_detik):
    menit = durasi_detik // 60
    detik = durasi_detik % 60
    return f"{menit}:{detik:02d}"

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    playlist.append((judul, artis, genre, durasi))
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.\n")
        return
        
    print("-" * 55)
    print(f"{'No':<3} {'Judul':<20} {'Artis':<15} {'Genre':<10} {'Durasi'}")
    print("-" * 55)
    
    total_durasi = 0
    for i, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        print(f"{i:<3} {judul:<20} {artis:<15} {genre:<10} {format_durasi(durasi)}")
        total_durasi += durasi
        
    print("-" * 55)
    total_menit = total_durasi // 60
    total_detik = total_durasi % 60
    print(f"Total durasi playlist: {total_menit} menit {total_detik} detik\n")

def filter_genre(playlist, genre_target):
    
    return [lagu for lagu in playlist if lagu[2] == genre_target]

def hapus_lagu(playlist, nomor):
    if 0 < nomor <= len(playlist):
        lagu_dihapus = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus dari playlist!\n")
    else:
        print("Nomor lagu tidak valid.\n")

def statistik_playlist(playlist, genre_set):
    if not playlist:
        print("Playlist kosong, tidak ada statistik.\n")
        return
        
    print("========================================")
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    print(f"Total lagu       : {len(playlist)}")
    print(f"Jumlah genre     : {len(genre_set)}")
    
    genre_format = "{'" + "', '".join(genre_set) + "'}" if genre_set else "{}"
    print(f"Daftar genre     : {genre_format}\n")
    
    print("Distribusi genre:")
    distribusi = {}
    for lagu in playlist:
        genre = lagu[2]
        distribusi[genre] = distribusi.get(genre, 0) + 1
        
    for genre, jumlah in distribusi.items():
        bar = "#" * jumlah
        print(f"  {genre:<14} : {bar} ({jumlah})")
        
    print()
    
    terpanjang = max(playlist, key=lambda x: x[3])
    terpendek = min(playlist, key=lambda x: x[3])
    
    print(f"Lagu terpanjang  : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f"Lagu terpendek   : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("========================================\n")

def main():
    playlist = []
    genre_set = set()
    
    print("========================================")
    print(" PLAYLIST MUSIK - PLAYTUNE")
    print("========================================")
    
    while True:
        print("\nMenu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            judul = input("Judul lagu: ")
            artis = input("Artis: ")
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
            
            while True:
                try:
                    durasi = int(input("Durasi (dalam detik): "))
                    if durasi > 0:
                        break
                    else:
                        print("Durasi harus angka positif!")
                except ValueError:
                    print("Input tidak valid! Masukkan angka.")
                    
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            
        elif pilihan == '2':
            print()
            tampilkan_playlist(playlist)
            
        elif pilihan == '3':
            if not genre_set:
                print("Belum ada genre yang tersedia.")
                continue
                
            print(f"Genre tersedia: {genre_set}")
            genre_target = input("Masukkan genre yang ingin difilter: ")
            
            hasil_filter = filter_genre(playlist, genre_target)
            
            print(f"\nLagu bergenre '{genre_target}':")
            if hasil_filter:
                for i, lagu in enumerate(hasil_filter, start=1):
                    print(f"  {i}. {lagu[0]} - {lagu[1]} ({format_durasi(lagu[3])})")
            else:
                print(f"Tidak ada lagu dengan genre {genre_target}")
            print()
                
        elif pilihan == '4':
            tampilkan_playlist(playlist)
            if playlist:
                try:
                    nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                    hapus_lagu(playlist, nomor)
                    
                    genre_set.clear()
                    for lagu in playlist:
                        genre_set.add(lagu[2])
                except ValueError:
                    print("Input tidak valid! Masukkan nomor angka.")
                    
        elif pilihan == '5':
            print()
            statistik_playlist(playlist, genre_set)
            
        elif pilihan == '6':
            print("Terima kasih telah menggunakan PlayTune!")
            break
            
        else:
            print("Pilihan menu tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()