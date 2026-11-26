
def deteksi_anomali_email(email):
    error = []

    jumlah_at = 0
    for karakter in email:
        if karakter == "@":
            jumlah_at += 1

    if jumlah_at != 1:
        error.append("Harus memiliki tepat satu karakter @.")

    if jumlah_at != 1:
        return error

    posisi_at = email.index("@")
    local = email[:posisi_at]
    domain = email[posisi_at + 1:]

    if local == "" or domain == "":
        error.append(
            "Bagian sebelum @ (local) atau setelah @ (domain) "
            "tidak boleh kosong."
        )

    ada_spasi = False
    for karakter in email:
        if karakter == " ":
            ada_spasi = True
            break

    if ada_spasi:
        error.append("Email tidak boleh mengandung spasi.")

    if local != "":
        if local[0] == "." or local[-1] == ".":
            error.append(
                "Bagian local tidak boleh diawali atau diakhiri titik."
            )

        if ".." in local:
            error.append(
                "Bagian local tidak boleh mengandung titik berurutan."
            )

    if domain != "":
        if "." not in domain:
            error.append("Bagian domain wajib memiliki minimal satu titik.")

        if ".." in domain or domain[-1] == ".":
            error.append(
                "Bagian domain tidak boleh mengandung titik berurutan "
                "atau diakhiri titik."
            )

    domain_resmi = (
        email.endswith(".com")
        or email.endswith(".id")
        or email.endswith(".ac.id")
    )

    if not domain_resmi:
        error.append(
            "Wajib berakhiran dengan .com, .id, atau .ac.id."
        )

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    panjang_maksimal = 0

    for email in daftar_email_valid:
        if len(email) > panjang_maksimal:
            panjang_maksimal = len(email)

    lebar = panjang_maksimal + 2

    garis = karakter_border * (lebar + 2)

    print("\n--- HASIL EMAIL VALID ---")
    print(garis)

    for email in daftar_email_valid:
        isi = " " + email.ljust(panjang_maksimal) + " "
        print(karakter_border + isi + karakter_border)

    print(garis)


def program_utama():
    print("--- Sistem Pencatatan Email Valid ---")

    karakter_border = input(
        "Masukkan border dengan karakter bebas: "
    )

    if karakter_border == "":
        karakter_border = "="
    else:
        karakter_border = karakter_border[0]

    print("\nKetik 'tutup' untuk mengakhiri masukan "
          "dan mencetak email.")

    daftar_email_valid = []

    while True:
        email = input("Masukkan email: ")

        if email.lower() == "tutup":
            break

        error = deteksi_anomali_email(email)

        if not error and email in daftar_email_valid:
            error.append("Email sudah terdaftar (Duplikat).")

        if error:
            print(">> Email DITOLAK karena:")
            for alasan in error:
                print("   -", alasan)
        else:
            daftar_email_valid.append(email)
            print(">> Email VALID!")

    cetak_daftar(daftar_email_valid, karakter_border)


program_utama()
