def konversi_suhu(suhu, skala_asal, skala_tujuan):
    if skala_asal == "C":
        celsius = suhu
    elif skala_asal == "F":
        celsius = (suhu - 32) * 5 / 9
    elif skala_asal == "K":
        celsius = suhu - 273.15
    else:
        raise ValueError("Skala suhu tidak dikenali.")

    if skala_tujuan == "C":
        hasil = celsius
    elif skala_tujuan == "F":
        hasil = (celsius * 9 / 5) + 32
    elif skala_tujuan == "K":
        hasil = celsius + 273.15
    else:
        raise ValueError("Skala suhu tidak dikenali.")

    return hasil


print("=== Konversi Suhu ===")

while True:
    suhu_input = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if suhu_input.lower() == "selesai":
        break

    suhu = float(suhu_input)

    skala_asal = input("Skala asal (C/F/K): ").upper()
    skala_tujuan = input("Skala tujuan (C/F/K): ").upper()

    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)

        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")

    except ValueError as e:
        print(f"Error: {e}")