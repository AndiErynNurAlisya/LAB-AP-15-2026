def cek_kata(teks,kata):
    teks_low = teks.lower()
    kata_low = kata.lower()
    list_indeks = []

    start = 0
    while True:
        indeks = teks_low.find(kata_low,start)
        if indeks == -1:
            break
        list_indeks.append(indeks)
        start = indeks + len(kata_low)
    return list_indeks

def cek_batas_kata(teks, i, panjang):
    teks_low = teks.lower()
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    if i > 0:
        char_sebelum = teks_low[i-1]
        if char_sebelum in alfabet:
            return False

    idx_setelah = i + panjang
    for i in range(len(teks_low)):
        char_setelah = teks_low[idx_setelah]
        if idx_setelah < len(teks_low):
            if char_setelah in alfabet:
                return False
    return True

def sensor_kata(teks, kata, simbol):
    semua_indeks = cek_kata(teks,kata)
    panjang_kata = len(kata)
    indeks_valid = []

    for idx in semua_indeks:
        if cek_batas_kata(teks, idx, panjang_kata):
            indeks_valid.append(idx)

    teks_tersensor = ""
    indeks_sekarang = 0

    for idx in indeks_valid:
        teks_tersensor += teks[indeks_sekarang:idx]
        teks_tersensor += simbol * panjang_kata
        indeks_sekarang = idx + panjang_kata
    teks_tersensor += teks[indeks_sekarang:]
    jumlah_tersensor = len(indeks_valid)

    return(teks_tersensor,jumlah_tersensor, indeks_valid)

teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks,kata,simbol)

print(f"Hasil Teks: {hasil}")
print(f"Jumlah: {jumlah} | Indeks: {indeks}")
        