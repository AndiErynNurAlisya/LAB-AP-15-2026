def deteksi_anomali_email(email, daftar_email_valid):
    errors = []
    
    if email in daftar_email_valid:
        errors.append("Email sudah terdaftar (Duplikat).")
        return errors

    if ' ' in email:
        errors.append("Tidak boleh mengandung spasi di posisi manapun.")
    
    if email.count('@') != 1:
        errors.append("Harus memiliki tepat satu karakter @.")
        return errors # Stop pengecekan komponen jika @ tidak valid
        
    local, domain = email.split('@')
    
    if not local or not domain:
        errors.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
        return errors

    if local.startswith('.') or local.endswith('.') or '..' in local:
        errors.append("Bagian local tidak boleh diawali atau diakhiri titik (.), serta tidak boleh mengandung titik berurutan (..).")
        
    if '..' in domain or domain.endswith('.'):
        errors.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
        
    if '.' not in domain:
        errors.append("Bagian domain wajib memiliki minimal satu titik.")
        
    domain_resmi = ('.com', '.id', '.ac.id')
    if not email.endswith(domain_resmi):
        errors.append("Wajib berakhiran dengan .com, .id, atau .ac.id")
        
    return errors


def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return ""
        
    max_len = max(len(email) for email in daftar_email_valid)
    lebar_bingkai = max_len + 4
    
    border_line = karakter_border * lebar_bingkai
    hasil = [border_line]
    
    for email in daftar_email_valid:
        hasil.append(f"{karakter_border} {email.ljust(max_len)} {karakter_border}")
        
    hasil.append(border_line)
    return "\n".join(hasil)


def main():
    print("--- Sistem Pencatatan email valid ---")
    karakter_border = input("Masukkan border dengan karakter bebas: ")
    print()
    
    daftar_email_valid = []
    
    while True:
        print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")
        email_input = input("Masukkan email: ")
        
        if email_input.strip() == 'tutup':
            break
            
        errors = deteksi_anomali_email(email_input, daftar_email_valid)
        
        if not errors:
            print(">> Email VALID!")
            daftar_email_valid.append(email_input)
        else:
            print(">> Email DITOLAK karena:")
            for err in errors:
                print(f"   - {err}")


if __name__ == "__main__":
    main()