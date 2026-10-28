def hitung_statistik_nilai(*nilai):
    if len(nilai)==0:
        return None

    rata_rata = sum(nilai) / len(nilai)    
    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)

    return rata_rata, nilai_tertinggi, nilai_terendah

def main():
    daftar_nilai = []

    while True:
        input_guru = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
        if input_guru == "":
            break

        daftar_nilai.append(float(input_guru))

    hasil_nilai = hitung_statistik_nilai(*daftar_nilai)
    if hasil_nilai is None:
         print("Data nilai tidak tersedia")
    else:
        rata,tinggi, rendah = hasil_nilai
        print(f"Rata rata nilai kelas : {rata}")
        print(f"Nilai tertinggi kelas : {tinggi}")
        print(f"Nilai terendah kelas  : {rendah}")
if __name__ == "__main__":
    main()