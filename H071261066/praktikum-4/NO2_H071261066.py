def hitung_statistik_ujian(*args):
    if len(args) == 0:
        return None

    rata_rata = sum(args) / len(args)
    nilai_tertinggi =  max(args)
    nilai_terendah = min(args)

    return rata_rata, nilai_tertinggi, nilai_terendah

daftar_nilai = []

while True:
    nilai_ujian = input("masukkan nilai ujian siswa (kosongkan jika selsai): ")

    if nilai_ujian == "":
        break

    try:
        nilai = float(nilai_ujian)
        if nilai.is_integer():
            nilai = int(nilai)
        daftar_nilai.append(nilai)
    except ValueError:
        print("input tidak valid, masukkan data atau kosongkan untuk selesai")

hasil = hitung_statistik_ujian(*daftar_nilai)

if hasil is None:
    print("data tidak valid")
else:
    rata_rata, nilai_tertinggi, nilai_terendah = hasil
    if isinstance(rata_rata, float) and rata_rata % 1 != 0:
        print(f"nilai rata rata: {rata_rata:.1f}")
    else:
        print(f"nilai rata rata: {int(rata_rata)}")
    
              
    print(f"nilai tertinggi: {nilai_tertinggi}")
    print(f"nilai terendah: {nilai_terendah}")