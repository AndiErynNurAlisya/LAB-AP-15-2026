def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""
    for karakter in teks:
        karakter_kecil = karakter.lower()
        if karakter_kecil in alfabet:
            teks_bersih += karakter_kecil
    return teks_bersih

def cek_palinrome(teks):
    teks_terbalik = "".join(reversed(teks))
    if teks == teks_terbalik:
        return True, -1
    else:
        for indeks_karakter in range(len(teks)):
            if teks[indeks_karakter] != teks_terbalik[indeks_karakter]:
                return False, indeks_karakter
        return False, -1

def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)
    panjang_maks = 0
    palinrome_terpanjang = ""
    indek_awal_terpanjang = 0 

    total_panjang_teks = len(teks_bersih)
    if total_panjang_teks == 0:
        return {"teks":"", "panjang": 0, "indeks_awal" : -1}
    
    for awal_potongan in range(total_panjang_teks):
        for akhir_potongan in range(awal_potongan + 1, total_panjang_teks + 1):
            substring = teks_bersih[awal_potongan:akhir_potongan]
            is_palinrome, _ = cek_palinrome(substring)

            if is_palinrome:
                panjang_substring = len(substring)
                if panjang_substring > panjang_maks:
                    panjang_maks = panjang_substring
                    palinrome_terpanjang = substring
                    indek_awal_terpanjang = awal_potongan
    return{
        "teks": palinrome_terpanjang,
        "panjang": panjang_maks,
        "indek_awal": indek_awal_terpanjang
    }


teks_input = input("Masukkan teks prasasti: ")
teks_bersih_hasil = bersihkan_teks(teks_input)
hasil = inti_palinrome(teks_input)

print(f"Teks Bersih: {teks_bersih_hasil}")
print(f"Output Terharap: {hasil}")


        










