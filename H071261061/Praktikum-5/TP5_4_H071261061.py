def deteksi_anomali_email(email, daftar_email_valid):
    pelanggaran = []

    if " " in email:
        pelanggaran.append("Tidak boleh mengandung spasi.")
        
    jumlah_at = email.count("@")
    if jumlah_at != 1:
        pelanggaran.append("Harus memiliki tepat satu karakter @.")
    else:
        local, domain = email.split("@")
        
        if not local or not domain:
            pelanggaran.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

        if local.startswith(".") or local.endswith("."):
            pelanggaran.append("Bagian local tidak boleh diawali atau diakhiri titik.")
        if ".." in local:
            pelanggaran.append("Bagian local tidak boleh mengandung titik berurutan.")
                
        if "." not in domain:
            pelanggaran.append("Bagian domain wajib memiliki minimal satu titik.")
        if ".." in domain or domain.endswith("."):
            pelanggaran.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    domain_resmi = (".com", ".id", ".ac.id")
    if not email.endswith(domain_resmi):
        pelanggaran.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    if email in daftar_email_valid:
        pelanggaran.append("e-mail sudah terdaftar (Duplikat)")

    return pelanggaran


def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return ""

    panjang_maksimal = max(len(email) for email in daftar_email_valid)
    lebar_dalam = panjang_maksimal + 2  # Padding spasi kiri dan kanan

    border_baris = "+" + (karakter_border * lebar_dalam) + "+"

    print(border_baris)
    for email in daftar_email_valid:
        print(f"| {email.ljust(panjang_maksimal)} |")
    print(border_baris)


print("--- Sistem Pencatatan email valid ---")
karakter_border = input("Masukkan border dengan karakter bebas: ")
print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_email_valid = []

while True:
    email_input = input("Masukkan email: ").strip()

    if email_input.lower() == "tutup":
        break

    pelanggaran = deteksi_anomali_email(email_input, daftar_email_valid)

    if not pelanggaran:
        print(">> Email VALID!")
        daftar_email_valid.append(email_input)
    else:
        print(">> Email DITOLAK karena:")
        for p in pelanggaran:
            print(f"   - {p}")

print("\n--- HASIL EMAIL VALID ---")
print(cetak_daftar(daftar_email_valid, karakter_border))