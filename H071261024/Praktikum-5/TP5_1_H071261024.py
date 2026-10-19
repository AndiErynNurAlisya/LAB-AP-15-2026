def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""

    for char in teks:
        char_low = char.lower()
        if char_low in alfabet:
            hasil += char_low
    return hasil

def cek_palinrome(teks):
    teks_reversed = "".join(reversed(teks))

    if teks == teks_reversed:
        return(True, -1)

    for i in range(len(teks)):
        if teks[i] != teks_reversed[i]:
            return(False, i)

def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)
    panjang_teks_bersih = len(teks_bersih)

    maks_len = 0
    best_pal = ""
    best_idx = 0

    for i in range(panjang_teks_bersih):
        for j in range(i+1, panjang_teks_bersih+1):
            substring = teks_bersih[i:j]
            is_pal = cek_palinrome(substring)[0]
            if is_pal:
                if len(substring) > maks_len:
                    maks_len = len(substring)
                    best_pal = substring
                    best_idx = i

    return{
        "teks": best_pal,
        "panjang": maks_len,
        "indeks_awal": best_idx
    }

teks = input("Masukkan teks prasasti: ")

print("\nTeks Bersih: ", bersihkan_teks(teks))
print("Output Terharap: ", inti_palinrome(teks))


