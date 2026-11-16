def cek_batas_kata(teks, i, panjang):
    if i == 0:
        batas_kiri = True
    else:
        char_kiri = teks[i - 1]
        batas_kiri = not (('a' <= char_kiri.lower() <= 'z') or ('0' <= char_kiri.lower() <= '9'))
    
    indeks_sesudah = i + panjang
    if indeks_sesudah == len(teks):
        batas_kanan = True
    else:
        char_kanan = teks[indeks_sesudah]
        batas_kanan = not (('a' <= char_kanan.lower() <= 'z') or ('0' <= char_kanan.lower() <= '9'))
        
    return batas_kiri and batas_kanan


def cek_kata(teks, kata):
    list_indeks = []
    i = 0
    n_teks = len(teks)
    n_kata = len(kata)
    
    while i <= n_teks - n_kata:
        cocok = True
        for j in range(n_kata):
            c1 = teks[i + j]
            c2 = kata[j]
            
            if 'A' <= c1 <= 'Z':
                c1 = chr(ord(c1) + 32)
            if 'A' <= c2 <= 'Z':
                c2 = chr(ord(c2) + 32)
            if c1 != c2:
                cocok = False
                break
        
        if cocok:
            if cek_batas_kata(teks, i, n_kata):
                list_indeks.append(i)
                i += n_kata
                continue
        i += 1
        
    return list_indeks


def sensor_kata(teks, kata, simbol):
    list_indeks_awal = cek_kata(teks, kata)
    n_kata = len(kata)
    simbol_pengganti = simbol * n_kata
    
    hasil_teks = ""
    indeks_sebelumnya = 0
    jumlah_tersensor = 0
    
    for idx in list_indeks_awal:
        bagian_sebelum = ""
        for k in range(indeks_sebelumnya, idx):
            bagian_sebelum += teks[k]
            
        hasil_teks += bagian_sebelum + simbol_pengganti
        indeks_sebelumnya = idx + n_kata
        jumlah_tersensor += 1
        
    sisa_teks = ""
    for k in range(indeks_sebelumnya, len(teks)):
        sisa_teks += teks[k]
    hasil_teks += sisa_teks
    
    return (hasil_teks, jumlah_tersensor, list_indeks_awal)

if __name__ == "__main__":
    teks_input = input("Masukkan Teks: ")
    kata_target = input("Masukkan kata target: ")
    simbol_input = input("Masukkan simbol: ")

    hasil_teks, jml, list_idx = sensor_kata(teks_input, kata_target, simbol_input)

    print(f"Hasil Teks: {hasil_teks}")
    print(f"Jumlah: {jml} | Indeks: {list_idx}")