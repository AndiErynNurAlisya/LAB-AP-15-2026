daftar_email_valid = []

def deteksi_anomali_email(email):
    errors = []
    if email.count('@') != 1 :
        errors.append("Harus memiliki tepat satu karakter @. ")
        return errors

    local, domain = email.split('@')

    if not local or not domain:
        errors.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if ' ' in email:
        errors.append("Tidak boleh mengandung spasi di posisi manapun.")

    if local.startswith('.') or local.endswith('.') or ('..') in local:
        errors.append("Bagian local tidak boleh diawali atau diakhiri titik (.), serta tidak boleh mengandung titik beruntun (..).")

    if ('.') not in domain:
        errors.append("Bagian domain wajib memiliki satu titik.")
    elif ('..') in domain or domain.endswith('.'):
        errors.append("Tidak boleh mengandung titik berurutan, dan tidak boleh diakhiri titik.")

    if email in daftar_email_valid:
        errors.append("Email sudah terdaftar (duplikat).")

    if not (email.endswith('.com') or email.endswith('.id') or email.endswith('.ac.id')):
        errors.append("Wajib berakhirann dengan salah satu domain resmi : .com, .id, .ac.ic")
    return errors

def cetak_daftar(daftar, karakter_border):
    print("\n--- HASIL EMAIL VALID ---")
    if not daftar:
        print("Tidak ada email yang valid")
        return

    max_len = max(len(email) for email in daftar)
    lebar_bingkai = max_len + 2

    border = "+" + (karakter_border * lebar_bingkai)

    print(border)
    for email in daftar:
        print (f"| {email:<{max_len}} |")
    print(border)


print("--- Sistem Pencatatan email valid ---")
karakter_border = input("Masukkan border dengan karakter bebas: ")
print("\nKetik 'tutup' untuk mengakhiri masukan dan menccetak email.")

while True:
    input_email = input("Masukkan email : ")
    if input_email.lower() == 'tutup':
        break

    daftar_error = deteksi_anomali_email(input_email)

    if len(daftar_error) > 0:
        print(">> Email DITOLAK karena: ")
        for error in daftar_error:
            print(f"  - {error}")
    else:
        print(">> Email Valid")
        daftar_email_valid.append(input_email)

cetak_daftar(daftar_email_valid, karakter_border)