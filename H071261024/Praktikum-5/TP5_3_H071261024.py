ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    is_upper = ch.isupper()
    ch_lower = ch.lower()

    idx = ALFABET.find(ch_lower)
    if idx == -1:
        return ch

    idx_baru = (idx + k) % 26
    hasil_ch = ALFABET[idx_baru]

    if is_upper:
        return hasil_ch.upper()
    else:
        return hasil_ch

def mesin_enkripsi(teks, k):
    teks_enkripsi = ""
    for ch in teks:
        teks_enkripsi += cek_sandi(ch, k)
    return teks_enkripsi

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil_retas = []

    for k in range(26):
        pesan_percobaan = mesin_dekripsi(sandi, k)

        if pesan_percobaan.lower().find(kata_kunci.lower()) != -1:
            hasil_retas.append((k, pesan_percobaan))

    return hasil_retas

pesan = input("Masukkan pesan tersita: ")
kata_kunci = input("Masukkan kata kunci target: ")

hasil = retas_sandi(pesan, kata_kunci)

print(f"Output Deskripsi: {hasil}")