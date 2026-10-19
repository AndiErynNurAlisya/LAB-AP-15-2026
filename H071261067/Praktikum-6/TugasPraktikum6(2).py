def daftar_kandidat(kandidat_set, nama):
    nama_cap = nama.capitalize()
    if nama_cap not in kandidat_set:
        kandidat_set.add(nama_cap)
        print(f"'{nama_cap}' berhasil didaftarkan sebagai kandidat!")
    else:
        print(f"'{nama_cap}' sudah terdaftar sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih_lower = nama_pemilih.lower()
    pilihan_cap = pilihan.capitalize()

    if nama_pemilih_lower in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    elif pilihan_cap not in kandidat_set:
        print(f"Kandidat '{pilihan_cap}' tidak terdaftar!")
    else:
        rekap_suara[nama_pemilih_lower] = pilihan_cap
        print(f"Suara '{nama_pemilih}' untuk '{pilihan_cap}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set}
    
    for suara in rekap_suara.values():
        if suara in perolehan:
            perolehan[suara] += 1
            
    return perolehan

def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)
    
    for kandidat, suara in sorted(perolehan.items()):
        print(f" {kandidat}: {suara} suara")
        
    total_suara = sum(perolehan.values())
    print(f"\nTotal suara masuk: {total_suara}")
    
    if total_suara > 0:
        max_suara = max(perolehan.values())
        pemenang = [k for k, v in perolehan.items() if v == max_suara]
        
        if len(pemenang) > 1:
            print(f"HASIL SERI antara {', '.join(pemenang)} dengan {max_suara} suara. Perlu pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {max_suara} suara!")
    else:
         print("Belum ada suara yang masuk, tidak ada pemenang.")
         
    print("=" * 40)

def main():
    print("========================================")
    print(" SISTEM PEMILIHAN KETUA KELAS")
    print("========================================\n")
    
    kandidat_set = set()
    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
        if not nama:
            if len(kandidat_set) >= 2:
                break
            else:
                print("Minimal harus ada 2 kandidat terdaftar untuk melanjutkan!")
                continue
        daftar_kandidat(kandidat_set, nama)

    print(f"\nKandidat terdaftar: {kandidat_set}\n")

    rekap_suara = {}
    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        print() 
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
        if not nama_pemilih:
            break
            
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    print() 
    
    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)

if __name__ == "__main__":
    main()