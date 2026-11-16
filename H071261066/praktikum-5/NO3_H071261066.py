ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    is_upper = ch.isupper()
    ch_lower = ch.lower()
    
    idx = ALFABET.find(ch_lower)
    
    if idx == -1:
        return ch
    
    new_idx = (idx + k) % 26
    new_ch = ALFABET[new_idx]
    
    return new_ch.upper() if is_upper else new_ch

def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil_retasan = []
    
    for k in range(26):
        teks_dekripsi = mesin_dekripsi(sandi, k)
        
        if teks_dekripsi.lower().find(kata_kunci.lower()) != -1:
            hasil_retasan.append((k, teks_dekripsi))
            
    return hasil_retasan

if __name__ == "__main__":
    pesan_tersita = input("Masukkan pesan tersita: ")
    kata_kunci = input("Masukkan kata kunci target: ")
    
    hasil = retas_sandi(pesan_tersita, kata_kunci)

    print(f"Output Deskripsi: {hasil}")