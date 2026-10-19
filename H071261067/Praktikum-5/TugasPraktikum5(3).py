ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    if ch.lower() not in ALFABET:
        return ch
    idx = ALFABET.find(ch.lower())

    idx_baru =(idx + k) % 26
    huruf_baru = ALFABET[idx_baru]

    if ch.isupper():
        return huruf_baru.upper()
    return huruf_baru

def mesin_enkripsi(teks, k):
    hasil_enkripsi = ""
    for ch in teks:
        hasil_enkripsi += cek_sandi(ch, k)
    return hasil_enkripsi

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil_retas =[]
    for k in range(26):
        teks_dekripsi = mesin_dekripsi(sandi, k)
        if teks_dekripsi.lower().find(kata_kunci.lower()) != -1:
            hasil_retas.append((k, teks_dekripsi))
    return hasil_retas

if __name__ == "__main__":
    pesan_persita = input("Masukkan Pesan Tersita(enkripsi Ceaser): ")
    kata_kunci = input("Masukkan kata kunci target: ")

    hasil = retas_sandi(pesan_persita, kata_kunci)

    print(f"Output Deskripsi: {hasil}")
