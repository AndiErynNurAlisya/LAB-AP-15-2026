def deteksi_anomali_email(email):
    list_error = []

    if " " in email:
        list_error.append("Tidak boleh ada spasi di email.")

    if email.count("@") != 1:
        list_error.append("Harus memiliki tepat satu karakter @.")
        return list_error

    local, domain = email.split("@")

    if len(local) == 0 or len(domain) == 0:
        list_error.append("Bagian local (sebelum @) dan domain (setelah @) tidak boleh kosong.")

    if len(local) > 0:
        if local.startswith(".") or local.endswith("."):
            list_error.append("Bagian local tidak boleh diawali atau diakhiri titik.")
        if ".." in local:
            list_error.append("Tidak boleh mengandung titik berurutan.")

    if len(domain) > 0:
        if "." not in domain:
            list_error.append("Bagian domain wajib memiliki minimal satu titik.") 
        if ".." in domain or domain.endswith(".") or domain.startswith("."):
            list_error.append("Domain tidak boleh mengandung titik berurutan serta tidak boleh diawali dan diakhiri oleh titik.")

    if not(email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")):
        list_error.append("Wajib berakhiran dengan salah satu domain resmi: .com, .id, atau .ac.id.")

    return list_error

def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        return 

    panjang_maks = 0
    for email in daftar_email_valid:
        if len(email) > panjang_maks:
            panjang_maks = len(email)

    print("\n--- HASIL EMAIL VALID ---")
    garis = "+" + (karakter_border * (panjang_maks + 2)) + "+"
    print(garis)

    for email in daftar_email_valid:
        sisa_spasi = " " * (panjang_maks - len(email))

        print(f"| {email}{sisa_spasi} |")
    print(garis)

print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_email_valid = []

while True:
    masukan = input("Masukkan email: ").strip()
    if masukan.lower() == "tutup":
        break
    if masukan in daftar_email_valid:
        print(">> Email DITOLAK karena:")
        print("- Email sudah terdaftar (Duplikat).\n")
        continue

    anomali = deteksi_anomali_email(masukan)

    if len(anomali) == 0:
        print(">> Email VALID!\n")
        daftar_email_valid.append(masukan)
    else:
        print(">> Email DITOLAK karena:")
        for err in anomali:
            print(f"- {err}")
        print()

cetak_daftar(daftar_email_valid, border)

    