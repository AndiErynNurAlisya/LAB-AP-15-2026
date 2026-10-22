def daftar_kandidat(kandidat_set, nama):
    nama_kandidat = nama.capitalize()
    kandidat_set.add(nama_kandidat)
    print(f"'{nama_kandidat}' berhasil didaftarkan sebagai kandidat!\n")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih_low = nama_pemilih.lower()
    yang_dipilih = pilihan.capitalize()

    if nama_pemilih_low in rekap_suara:
        print(f"'{nama_pemilih.capitalize()}' sudah memberikan suara sebelumnya!")
        return

    if yang_dipilih not in kandidat_set:
        print("Error: Kandidat tidak terdaftar!")
        return

    rekap_suara[nama_pemilih_low] = yang_dipilih
    print(f"Suara '{nama_pemilih.capitalize()}' untuk '{yang_dipilih}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        if pilihan in perolehan:
            perolehan[pilihan] += 1

    return perolehan

def tampilkan_hasil(perolehan):
    garis = "=" * 40
    print(f"\n{garis}")
    print("  HASIL PEMILIHAN KETUA KELAS")
    print(garis)

    total_suara_masuk = 0
    suara_tertinggi = -1
    pemenang_list = []

    for kandidat, jumlah in perolehan.items():
        print(f"  {kandidat}: {jumlah} suara")
        total_suara_masuk += jumlah

        if jumlah > suara_tertinggi:
            suara_tertinggi = jumlah
            pemenang_list = [kandidat]
        elif jumlah == suara_tertinggi:
            pemenang_list.append(kandidat)

    print(f"Total suara masuk: {total_suara_masuk}")

    if len(pemenang_list) > 1 and suara_tertinggi > 0:
        print(f"Hasil SERI antara: {', '.join(pemenang_list)}")
        print("Perlu dilakukan pemilihan ulang!")
    elif suara_tertinggi == 0:
        print("Belum ada suara yang masuk!")
    else:
        print(f"PEMENANG: {pemenang_list[0]} dengan {suara_tertinggi} suara!")
    print(garis)

kandidat_set = set()
rekap_suara = {}
garis = "=" * 40
print(garis)
print("  SISTEM PEMILIHAN KETUA KELAS")
print(garis)

print("\n--- FASE PENDAFTARAN KANDIDAT ---")
while True:
    nama = input("\nMasukkan nama kandidat (kosongkan untuk selesai): ").strip()
    if nama == "":
        if len(kandidat_set) < 2:
            print("Kandidat harus lebih dari 1!")
            continue
        break
    daftar_kandidat(kandidat_set, nama)
print(f"\nKandidat terdaftar: {kandidat_set}")

print("\n--- FASE PEMUNGUTAN SUARA ---")
while True:
    nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ").strip()
    if nama_pemilih == "":
        break

    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ").strip()
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)