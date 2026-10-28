def bersihkan_teks(teks):
    text = teks.lower()
    for i in text:
        if i not in 'abcdefghijklmnopqrstuvwxyz':
            text = text.replace(i, '')
    return text


def cek_palinrome(teks):
    teks_balik = "".join(reversed(teks))

    if teks == teks_balik:
        return (True, -1)

    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return (False, i)


def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)

    palindrom_terpanjang = ""
    indeks_awal = 0

    for i in range(len(teks_bersih)):
        for j in range(i, len(teks_bersih) + 1):

            substring = teks_bersih[i:j]

            hasil_cek, _ = cek_palinrome(substring)

            if hasil_cek == True:
                if len(substring) > len(palindrom_terpanjang):
                    palindrom_terpanjang = substring
                    indeks_awal = i

    return {
        "teks": palindrom_terpanjang,
        "panjang": len(palindrom_terpanjang),
        "indeks_awal": indeks_awal
    }


teks = input("Masukkan teks prasasti: ")
hasil = inti_palinrome(teks)

teks_bersih = bersihkan_teks(teks)
print()
print("Teks Bersih:", teks_bersih)
print("Output Terharap:", hasil)