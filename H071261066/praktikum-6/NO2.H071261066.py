def daftar_kandidat(kandidat_set, nama):
    nama_clean = nama.strip().capitalize()
    if nama_clean:
        kandidat_set.add(nama_clean)
        print(f"'{nama_clean}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih_clean = nama_pemilih.strip().lower()
    pilihan_clean = pilihan.strip().capitalize()
    
    if nama_pemilih_clean in rekap_suara:
        print(f"'{nama_pemilih.strip()}' sudah memberikan suara sebelumnya!")
        return

    if pilihan_clean not in kandidat_set:
        print("Kandidat tidak valid, suara tidak dicatat.")
        return

    rekap_suara[nama_pemilih_clean] = pilihan_clean
    print(f"Suara '{nama_pemilih.strip()}' untuk '{pilihan_clean}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set}
    
    for kandidat_pilihan in rekap_suara.values():
        if kandidat_pilihan in perolehan:
            perolehan[kandidat_pilihan] += 1
            
    return perolehan

def tampilkan_hasil(perolehan):
    print("\n===============================")
    print("HASIL PEMILIHAN KETUA KELAS")
    print("===============================")
    
    total_suara = 0
    maks_suara = -1
    pemenang = []

    
    for kandidat, suara in perolehan.items():
        print(f"{kandidat}: {suara} suara")
        total_suara += suara
        
        if suara > maks_suara:
            maks_suara = suara
            pemenang = [kandidat]
        elif suara == maks_suara:
            pemenang.append(kandidat)

    print("-------------------------------")
    print(f"Total suara masuk: {total_suara}")
    
    if len(pemenang) == 1:
        print(f"PEMENANG: {pemenang[0]} dengan {maks_suara} suara!")
    else:
        kandidat_seri = ", ".join(pemenang)
        print(f"Hasil SERI antara: {kandidat_seri}")
        print("Perlu dilakukan pemilihan ulang!")
    print("===============================")

def main():
    print("SISTEM PEMILIHAN KETUA KELAS")
    print("=============================\n")
    
    # 1
    print("--- FASE PENDAFTARAN KANDIDAT ---")
    kandidat_set = set()
    
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
        if nama.strip() == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum bisa lanjut.")
                continue
            else:
                break
        daftar_kandidat(kandidat_set, nama)
        
    print(f"\nKandidat terdaftar: {kandidat_set}\n")
    
    # 2
    print("--- FASE PEMUNGUTAN SUARA ---")
    rekap_suara = {} 
    
    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
        if nama_pemilih.strip() == "":
            break
            
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)
        print() 
    # 3
    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)

if __name__ == "__main__":
    main()