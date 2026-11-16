def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    
    for g in genre.split(","):
        genre_set.add(g.strip()) 
        
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!\n")

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist kosong.\n")
        return
    
    print("\n" + "="*65)
    print(f"{'No':<3} {'Judul':<20} {'Artis':<15} {'Genre':<15} {'Durasi':<8}")
    print("="*65)
    
    total_detik = 0
    for idx, (judul, artis, genre, durasi) in enumerate(playlist, 1):
        menit = durasi // 60
        detik = durasi % 60
        durasi_str = f"{menit}:{detik:02d}"
        
        print(f"{idx:<3} {judul:<20} {artis:<15} {genre:<15} {durasi_str:<8}")
        total_detik += durasi
        
    total_menit = total_detik // 60
    sisa_detik = total_detik % 60
    print("="*65)
    print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik\n")

def filter_genre(playlist, genre_target):
    filtered = [lagu for lagu in playlist if genre_target.lower() in lagu[2].lower()]
    return filtered

def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu_dihapus = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus.\n")
    else:
        print("Nomor lagu tidak valid.\n")

def statistik_playlist(playlist, genre_set):
    if not playlist:
        print("Playlist kosong, tidak ada statistik.\n")
        return
    
    total_lagu = len(playlist)
    jumlah_genre_unik = len(genre_set)
    
    distribusi_genre = {}
    for lagu in playlist:
        list_g = [g.strip() for g in lagu[2].split(",")]
        
        for genre_tunggal in list_g:
            distribusi_genre[genre_tunggal] = distribusi_genre.get(genre_tunggal, 0) + 1
        
    # Menentukan lagu terpanjang dan terpendek berdasarkan durasi (elemen indeks ke-3)
    lagu_terpanjang = max(playlist, key=lambda x: x[3])
    lagu_terpendek = min(playlist, key=lambda x: x[3])
    
    print("\n" + "="*30)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("="*30)
    print(f"Total lagu        : {total_lagu}")
    print(f"Jumlah genre      : {jumlah_genre_unik}")
    print(f"Daftar genre      : {genre_set}")
    print("\nDistribusi genre:")
    for gen, count in distribusi_genre.items():
        print(f"  {gen:<15} : # ({count})")
        
    def format_lagu(lagu):
        menit = lagu[3] // 60
        detik = lagu[3] % 60
        return f"{lagu[0]} - {lagu[1]} ({menit}:{detik:02d})"
        
    print(f"\nLagu terpanjang   : {format_lagu(lagu_terpanjang)}")
    print(f"Lagu terpendek    : {format_lagu(lagu_terpendek)}")
    print("="*30 + "\n")

def main():
    playlist = []
    genre_set = set()
    
    while True:
        print("======= PLAYLIST MUSIK - PLAYTUNE =======")
        print("Menu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter Berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ").strip()
        
        if pilihan == '1':
            judul = input("Judul lagu: ").strip()
            artis = input("Artis: ").strip()
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
            genre = ", ".join(set(g.strip() for g in genre.split(",")))
            
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    raise ValueError
            except ValueError:
                print("Input tidak valid! Durasi harus berupa angka bulat positif.\n")
                continue
                
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            
        elif pilihan == '2':
            tampilkan_playlist(playlist)
            
        elif pilihan == '3':
            if not genre_set:
                print("Belum ada genre yang tersedia.\n")
                continue
            print(f"Genre tersedia: {genre_set}")
            genre_target = input("Masukkan genre yang ingin difilter: ").strip()
            
            hasil_filter = filter_genre(playlist, genre_target)
            print(f"\nLagu bergenre '{genre_target}':")
            if not hasil_filter:
                print("Tidak ada lagu dengan genre tersebut.\n")
            else:
                for idx, lagu in enumerate(hasil_filter, 1):
                    menit = lagu[3] // 60
                    detik = lagu[3] % 60
                    print(f"{idx}. {lagu[0]} - {lagu[1]} ({menit}:{detik:02d})")
                print()
                
        elif pilihan == '4':
            tampilkan_playlist(playlist)
            if not playlist:
                continue
            try:
                nomor = int(input("Minta nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)
            except ValueError:
                print("Input harus berupa angka.\n")
                
        elif pilihan == '5':
            statistik_playlist(playlist, genre_set)
            
        elif pilihan == '6':
            print("Terima kasih telah menggunakan PlayTune!")
            break
        else:
            print("Pilihan menu tidak valid. Silakan coba lagi.\n")

if __name__ == "__main__":
    main()