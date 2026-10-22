detik_ke_menit = lambda detik: f"{detik // 60}:{detik % 60:02d}"

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu_tuple = (judul, artis, genre, durasi)
    playlist.append(lagu_tuple)
    
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        return

    garis = "=" * 45
    print(f"\n{garis}")
    print(f"{'No':<4} {'Judul':<20} {'Artis':<15} {'Genre':<10} {'Durasi':<6}")
    print(garis)
    
    total_detik_seluruhnya = 0
    for i in range(len(playlist)):
        lagu = playlist[i]
        judul, artis, genre, durasi = lagu
        
        nomor_tampil = i + 1
        
        total_detik_seluruhnya += durasi
        durasi_str = detik_ke_menit(durasi)
        print(f"{nomor_tampil:<4} {judul:<20} {artis:<15} {genre:<10}{durasi_str:<6}")
        
    print(garis)
    total_menit = total_detik_seluruhnya // 60
    sisa_detik = total_detik_seluruhnya % 60
    print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik")

def filter_genre(playlist, genre_target):
    hasil_filter = [lagu for lagu in playlist if lagu[2] == genre_target]
    return hasil_filter

def hapus_lagu(playlist, nomor):
    try:
        indeks = nomor - 1
        lagu_terhapus = playlist.pop(indeks)
        print(f"Lagu '{lagu_terhapus[0]}' berhasil dihapus dari playlist.")
    except IndexError:
        print("Error: Nomor lagu tidak ditemukan di playlist!")

def statistik_playlist(playlist, genre_set):
    if not playlist:
        print("Playlist kosong, belum ada statistik.")
        return

    total_lagu = len(playlist)
    jumlah_genre = len(genre_set)
    
    distribusi = {}
    for genre in genre_set:
        hitung = 0
        for lagu in playlist:
            if lagu[2] == genre:
                hitung += 1
        distribusi[genre] = hitung
        
    lagu_terpanjang = max(playlist, key=lambda x: x[3])
    lagu_terpendek = min(playlist, key=lambda x: x[3])

    garis = "=" * 40
    print(f"\n{garis}")
    print("STATISTIK PLAYLIST PLAYTUNE")
    print(garis)
    print(f"Total lagu        : {total_lagu}")
    print(f"Jumlah genre      : {jumlah_genre}")
    print(f"Daftar genre      : {genre_set}")
    print("\nDistribusi genre  :")
    for genre, jumlah in distribusi.items():
        bar_visual = "#" * jumlah
        print(f"  {genre:<15}: {bar_visual} ({jumlah})")
    print(f"\nLagu terpanjang   : {lagu_terpanjang[0]} ({detik_ke_menit(lagu_terpanjang[3])})")
    print(f"Lagu terpendek    : {lagu_terpendek[0]} ({detik_ke_menit(lagu_terpendek[3])})")
    print(garis)

playlist = []
genre_set = set()

garis = "=" * 40
print(garis)
print("  PLAYLIST MUSIK - PLAYTUNE")
print(garis)

while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")
    
    pilihan_menu = input("Pilih menu (1-6): ").strip()
    
    if pilihan_menu == "1":
        judul = input("Judul lagu: ").strip().capitalize()
        artis = input("Artis: ").strip().capitalize()
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip().capitalize()
        
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                print("Error: Durasi harus berupa angka positif!")
                continue
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        except ValueError:
            print("Error: Durasi harus berupa angka bulat (integer)!")
            
    elif pilihan_menu == "2":
        tampilkan_playlist(playlist)
        
    elif pilihan_menu == "3":
        if not genre_set:
            print("Belum ada genre yang tersedia.")
        else:
            print(f"Genre tersedia: {genre_set}")
            target = input("Masukkan genre yang ingin difilter: ").strip().capitalize()
            hasil = filter_genre(playlist, target)
            if not hasil:
                print(f"Tidak ada lagu dengan genre '{target}'.")
            else:
                print(f"\nLagu bergenre '{target}':")
                for i in range(len(hasil)):
                    l = hasil[i]
                    print(f"{i + 1}. {l[0]} - {l[1]} ({detik_ke_menit(l[3])})")
                    
    elif pilihan_menu == "4":
        if not playlist:
            print("Playlist kosong.")
        else:
            tampilkan_playlist(playlist)
            try:
                nomor_hapus = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor_hapus)
            except ValueError:
                print("Error: Masukkan angka nomor lagu yang valid!")
                
    elif pilihan_menu == "5":
        statistik_playlist(playlist, genre_set)
        
    elif pilihan_menu == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break
    else:
        print("Pilihan tidak valid, silakan pilih menu 1 sampai 6.")