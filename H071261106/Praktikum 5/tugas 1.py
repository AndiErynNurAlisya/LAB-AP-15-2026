
def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""

    for karakter in teks:
        karakter = karakter.lower()

        if karakter in alfabet:
            hasil += karakter

    return hasil


def cek_palindrome(teks):
    kiri = 0
    kanan = len(teks) - 1

    while kiri < kanan:
        if teks[kiri] != teks[kanan]:
            return False, kiri

        kiri += 1
        kanan -= 1

    return True, -1


def inti_palindrome(teks):
    hasil = {
        "teks": "",
        "panjang": 0,
        "indeks_awal": 0
    }

    panjang_teks = len(teks)

    for panjang in range(panjang_teks, 0, -1):
        for awal in range(panjang_teks - panjang + 1):
            substring = teks[awal:awal + panjang]
            simetris, indeks = cek_palindrome(substring)

            if simetris:
                hasil = {
                    "teks": substring,
                    "panjang": panjang,
                    "indeks_awal": awal
                }

                return hasil

    return hasil


teks = input("Masukkan teks prasasti: ")

teks_bersih = bersihkan_teks(teks)
hasil = inti_palindrome(teks_bersih)

print("\nTeks Bersih:", teks_bersih)
print("Output Terharap:", hasil)
