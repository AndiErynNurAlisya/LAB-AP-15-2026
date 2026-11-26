def format_durasi(detik):
    """Fungsi pembantu untuk mengonversi durasi detik ke format menit:detik"""
    menit = detik // 60
    sisa_detik = detik % 60
    return f"{menit}:{sisa_detik:02d}"

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    """Menambahkan lagu baru ke playlist dan genre ke genre_set"""
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    """Menampilkan seluruh lagu dalam playlist dalam format tabel"""
    if not playlist:
        print("\nPlaylist masih kosong.")
        return

    print("=" * 60)
    print(f"{'No':<4} {'Judul':<25} {'Artis':<15} {'Genre':<10} {'Durasi':<6}")
    print("=" * 60)
    
    total_detik = 0
    for i, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        durasi_str = format_durasi(durasi)
        print(f"{i:<4} {judul:<25} {artis:<15} {genre:<10} {durasi_str:<6}")
        total_detik += durasi
        
    print("=" * 60)
    
    total_menit = total_detik // 60
    sisa_detik = total_detik % 60
    print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik")

def filter_genre(playlist, genre_target):
    """Memfilter lagu berdasarkan genre menggunakan list comprehension"""
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]

def hapus_lagu(playlist, nomor):
    """Menghapus lagu dari playlist berdasarkan nomor/indeks"""
    if 1 <= nomor <= len(playlist):
        lagu_dihapus = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus dari playlist!")
    else:
        print("Nomor lagu tidak valid.")

def statistik_playlist(playlist, genre_set):
    """Menampilkan statistik lengkap dari playlist"""
    if not playlist:
        print("\nBelum ada data statistik (playlist kosong).")
        return

    print("=" * 60)
    print("  STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 60)
    
    print(f"Total lagu       : {len(playlist)}")
    print(f"Jumlah genre     : {len(genre_set)}")
    print(f"Daftar genre     : {genre_set}")
    print("\nDistribusi genre :")
    
    hitung_genre = {}
    for _, _, genre, _ in playlist:
        hitung_genre[genre] = hitung_genre.get(genre, 0) + 1
        
    for g, jumlah in hitung_genre.items():
         visual = "#" * jumlah
         print(f"  {g:<15}: {visual} ({jumlah})")
        
    lagu_terpanjang = max(playlist, key=lambda x: x[3])
    lagu_terpendek = min(playlist, key=lambda x: x[3])
    
    durasi_max_str = format_durasi(lagu_terpanjang[3])
    durasi_min_str = format_durasi(lagu_terpendek[3])
    
    print(f"\nLagu terpanjang : {lagu_terpanjang[0]} ({durasi_max_str})")
    print(f"Lagu terpendek  : {lagu_terpendek[0]} ({durasi_min_str})")
    print("=" * 60)

def main():
    playlist = []
    genre_set = set()

    while True:
        print("\n==============================================")
        print("  PLAYLIST MUSIK - PLAYTUNE")
        print("==============================================")
        print("Menu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ").strip()
        
        if pilihan == "1":
            judul = input("Judul lagu: ").strip()
            artis = input("Artis: ").strip()
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
            
            while True:
                try:
                    durasi = int(input("Durasi (dalam detik): "))
                    if durasi > 0:
                        break
                    else:
                        print("Durasi harus berupa angka positif!")
                except ValueError:
                    print("Input tidak valid! Masukkan angka bulat untuk durasi.")
            
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)

        elif pilihan == "2":
            tampilkan_playlist(playlist)

        elif pilihan == "3":
            if not playlist:
                print("Playlist kosong, belum ada genre yang tersedia.")
                continue
            print(f"Genre tersedia: {genre_set}")
            genre_target = input("Masukkan genre yang ingin difilter: ").strip()
            
            hasil_filter = filter_genre(playlist, genre_target)
            if hasil_filter:
                print(f"\nLagu bergenre '{genre_target}':")
                for idx, (j, a, g, d) in enumerate(hasil_filter, start=1):
                    print(f"  {idx}. {j} - {a} ({format_durasi(d)})")
            else:
                print(f"Tidak ada lagu dengan genre '{genre_target}'.")

        elif pilihan == "4":
            tampilkan_playlist(playlist)
            if playlist:
                try:
                    nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                    hapus_lagu(playlist, nomor)
                except ValueError:
                    print("Input harus berupa angka nomor urut lagu.")

        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)

        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break

        else:
            print("Pilihan menu tidak valid. Silakan pilih 1-6.")

if __name__ == "__main__":
    main()