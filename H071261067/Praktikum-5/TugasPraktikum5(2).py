def cek_kata(teks, kata):
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    indeks_list = []
    start = 0

    while True:
        idx = teks_lower.find(kata_lower, start)
        if idx == -1:
            break
        indeks_list.append(idx)
        start = idx + len(kata)
    return indeks_list

def cek_batas_kata(teks, i, panjang):
    is_valid_before = True
    is_valid_after = True

    if i > 0:
        char_before = teks[i-1]
        if ('a' <= char_before <= 'z') or ('A' <= char_before <= 'Z'):
            is_valid_before = False

    if i + panjang < len(teks):
        char_after = teks[i+panjang]
        if ('a' <= char_after <= 'z') or ('A' <= char_after <= 'Z'):
            is_valid_after = False

    return is_valid_before and is_valid_after

def sensor_kata(teks, kata, simbol):
    semua_indeks = cek_kata(teks, kata)
    panjang_kata = len(kata)
    list_indeks_awal = []

    for idx in semua_indeks:
        if cek_batas_kata(teks, idx, panjang_kata):
            list_indeks_awal.append(idx)

    teks_tersensor = ""
    jumlah_tersensor = len(list_indeks_awal)
    posisi_sekarang = 0

    for idx in list_indeks_awal:
        teks_tersensor += teks[posisi_sekarang:idx]
        teks_tersensor += simbol * panjang_kata
        posisi_sekarang = idx + panjang_kata

    teks_tersensor += teks[posisi_sekarang:]

    return teks_tersensor, jumlah_tersensor, list_indeks_awal

if __name__ == "__main__":
    teks_input = input("Masukkan Teks: ")
    kata_target = input("Masukkan Kata Target: ")
    simbol = input("Masukkan simbol: ")

    hasil_teks, jumlah, indeks = sensor_kata(teks_input, kata_target, simbol)

    print(f"Hasil Teks: ", {hasil_teks})
    print(f"Jumlah: {jumlah} | Indeks: {indeks}" )
