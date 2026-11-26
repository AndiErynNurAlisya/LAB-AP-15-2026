
ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    kapital = ch.isupper()
    huruf = ch.lower()

    if huruf not in ALFABET:
        return ch

    indeks = ALFABET.index(huruf)
    indeks_baru = (indeks + k) % 26
    hasil = ALFABET[indeks_baru]

    if kapital:
        return hasil.upper()

    return hasil


def mesin_enkripsi(teks, k):
    hasil = ""

    for ch in teks:
        hasil += cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    hasil = []
    kata_kunci = kata_kunci.lower()

    for kunci in range(26):
        pesan_asli = mesin_dekripsi(sandi, kunci)

        if kata_kunci in pesan_asli.lower():
            hasil.append((kunci, pesan_asli))

    return hasil


sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")

hasil = retas_sandi(sandi, kata_kunci)

print("\nOutput Deskripsi:", hasil)
