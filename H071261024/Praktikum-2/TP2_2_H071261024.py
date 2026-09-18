jarak = float(input("Masukkan jarak pengiriman (km): "))
layanan = input("Layanan express (ya/tidak): ").lower()

if jarak <= 0:
    print("Tidak valid")
else:
    if jarak < 5:
        tarif_dasar = 10000
    elif 5 <= jarak <= 20:
        tarif_dasar = 20000
    else:
        tarif_dasar = 35000

    BIAYA_TAMBAHAN = 15000 if layanan == "ya" else 0

    total_tarif = tarif_dasar + BIAYA_TAMBAHAN

    print(f"Total tarif pengiriman: Rp{total_tarif:,}")