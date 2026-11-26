
def cek_kata(teks, kata):
    indeks = []
    kata = kata.lower()
    teks_kecil = teks.lower()
    panjang_kata = len(kata)

    if panjang_kata == 0:
        return indeks

    for i in range(len(teks) - panjang_kata + 1):
        cocok = True

        for j in range(panjang_kata):
            if teks_kecil[i + j] != kata[j]:
                cocok = False
                break

        if cocok:
            indeks.append(i)

    return indeks


def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    if i > 0:
        sebelum = teks[i - 1].lower()

        if sebelum in alfabet:
            return False

    akhir = i + panjang

    if akhir < len(teks):
        sesudah = teks[akhir].lower()

        if sesudah in alfabet:
            return False

    return True


def sensor_kata(teks, kata, simbol):
    indeks_kemunculan = cek_kata(teks, kata)
    panjang_kata = len(kata)

    if panjang_kata == 0:
        return teks, 0, []

    hasil = ""
    indeks_awal = []
    jumlah = 0
    i = 0

    while i < len(teks):
        cocok = False

        for indeks in indeks_kemunculan:
            if i == indeks:
                cocok = True
                break

        if cocok and cek_batas_kata(teks, i, panjang_kata):
            hasil += simbol * panjang_kata
            indeks_awal.append(i)
            jumlah += 1
            i += panjang_kata
        else:
            hasil += teks[i]
            i += 1

    return hasil, jumlah, indeks_awal


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

teks_sensor, jumlah, indeks = sensor_kata(
    teks, kata, simbol
)

print("Hasil Teks:", teks_sensor)
print("Jumlah:", jumlah, "| Indeks:", indeks)
