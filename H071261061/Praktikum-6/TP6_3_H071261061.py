def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)

    genre_set.add(genre)

    playlist.append(lagu)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!\n")

def tampilkan_playlist(playlist):
    print("\n=========================================================")
    print(" No\tJudul\t\tArtis\t\tGenre\tDurasi ")
    print("=========================================================")
    total_durasi = 0
    for i, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu
        total_durasi += durasi
        menit = durasi // 60
        detik = durasi % 60
        print(f" {i}.\t{judul}\t\t{artis}\t\t{genre}\t{menit}:{detik}")
    print("=========================================================")
    totalmenit = total_durasi // 60
    totaldetik = total_durasi % 60
    print(f" Total durasi playlist: {totalmenit} menit {totaldetik} detik\n")

def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if genre_target.lower() == lagu[2].lower()]

def hapus_lagu(playlist, nomor):
    hapus = playlist.pop(nomor)
    print(f"Lagu {hapus[0]} berhasil dihapus!")

def statistik_playlist(playlist, genre_set):
    print("========================================")
    print("  STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    print(f"  Total lagu      : {len(playlist)}")
    print(f"  Jumlah genre    : {len(genre_set)}")
    print(f"  Daftar genre    : {genre_set}\n")
    print("  Distribusi genre:")
    distribusi = {}
    for genre in genre_set:
        distribusi[genre] = 0 
    for lagu in playlist:
        if lagu[2] in distribusi:
            distribusi[lagu[2]] += 1 
    for lagu, total in distribusi.items():    
        print(f"    {lagu}        : # ({total})")
    laguterpanjang = playlist[0]
    laguterpendek = playlist[0]
    for lagu in playlist:
        terpanjang = laguterpanjang[3]
        terpendek = laguterpendek[3]
        if lagu[3] > terpanjang:
            laguterpanjang = lagu
        if lagu[3] < terpendek:
            laguterpendek = lagu
    menitterpanjang, detikterpanjang = laguterpanjang[3]//60, laguterpanjang[3] % 60
    menitterpendek, detikterpendek = laguterpendek[3]//60, laguterpendek[3] % 60
    print(f"\n  Lagu terpanjang : {laguterpanjang[0]} ({menitterpanjang}:{detikterpanjang})")
    print(f"  Lagu terpendek : {laguterpendek[0]} ({menitterpendek}:{detikterpendek})")
    print("========================================\n")


playlist = []
genre_set = set()

print("========================================")
print("   PLAYLIST MUSIK - PLAYTUNE")
print("========================================\n")
print("Menu:")
print("1. Tambah Lagu ")
print("2. Tampilkan Playlist ")
print("3. Filter berdasarkan Genre ")
print("4. Hapus Lagu")
print("5. Statistik Playlist ")
print("6. Keluar")

while True:
    menu = input("Pilih menu (1-6): ")

    if menu == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi < 0:
                print("Durasi tidak boleh mines!")
                continue
        except ValueError:
            print("Durasi harus berupa angka!")
        tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)

    elif menu == "2":
        if not playlist:
            print("Tidak ada lagu!")
        else:
            tampilkan_playlist(playlist)

    elif menu == "3":
        if not playlist:
            print("Belum ada lagu!")
        else:
            print(f"Genre tersedia: {genre_set}")
            genre_target = input("Masukkan genre yang ingin difilter: ")
            lagu = filter_genre(playlist, genre_target)
            print(f"Lagu bergenre '{genre_target}':")
            for k, isi in enumerate(lagu, 1):
                menitlagu = isi[3]//60
                detiklaggu = isi[3]%60
                print(f"  {k}. {isi[0]} - {isi[1]} ({menitlagu}:{detiklaggu})")
        print()

    elif menu == "4":
        if not playlist:
            print("Belum ada lagu!")
        else:
            tampilkan_playlist(playlist)          
            nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
            if len(playlist) < nomor < 1:
                print("Lagu tidak ada!")
            else:
                hapus_lagu(playlist, nomor)

    elif menu == "5":
        if not playlist:
            print("Belum ada lagu!")
        else:
            statistik_playlist(playlist, genre_set)

    elif menu == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break
    else:
        print("input tidak valid!")
