def rekap_nilai(*nilai: float) -> None:
    if len(nilai) == 0:
        return None

    rata_rata = sum(nilai)/len(nilai)
    tertinggi = max(nilai)
    terendah = min(nilai)

    return rata_rata, tertinggi, terendah

def main_rekap() -> None:
    daftar_nilai = []

    while True:
        input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
        if input_nilai == "":
            break

        nilai = float(input_nilai)
        if nilai == int(nilai):
            nilai = int(nilai)

        daftar_nilai.append(nilai)

    hasil = rekap_nilai(*daftar_nilai)
    if hasil == None:
        print("Data tidak tersedia!")
    else:
        rata_rata, tertinggi, terendah = hasil
        print(f"Rata-rata kelas: {rata_rata}")
        print(f"Nilai tertinggi: {tertinggi}")
        print(f"Nilai terendah: {terendah}")

main_rekap()