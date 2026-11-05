def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""
    for char in teks:
        char_lower = char.lower()
        if char_lower in alfabet:
            teks_bersih += char_lower
    return teks_bersih

def cek_palinrome(teks):
    teks_reversed = "".join(reversed(teks))
    if teks == teks_reversed:
        return (True, -1)
    else:
        for i in range(len(teks)):
            if teks[i] != teks_reversed[i]:
                return (False, i)

def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)
    max_len = 0
    hasil = {"teks": "", "panjang": 0, "indeks_awal": 0}
    
    for i in range(len(teks_bersih)):
        for j in range(i + 1, len(teks_bersih) + 1):
            substring = teks_bersih[i:j]
            is_pal, _ = cek_palinrome(substring)
            
            if is_pal:
                if len(substring) > max_len:
                    max_len = len(substring)
                    hasil = {
                        "teks": substring,
                        "panjang": max_len,
                        "indeks_awal": i
                    }
    return teks_bersih, hasil

input_masukan = input("Masukkan teks prasasti: ")

teks_bersih, output_terharap = inti_palinrome(input_masukan)

print("Teks Bersih:", teks_bersih)
print("Output Terharap:", output_terharap)