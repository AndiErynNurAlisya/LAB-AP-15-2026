def konversi_suhu(suhu: float, asal: str, tujuan: str) -> float:
    skala_valid = ["C", "F", "K"]
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali!")

    if asal == tujuan:
        return suhu

    #Semua skala ke Celcius
    if asal == "C":
        skala_celcius = suhu
    elif asal == "F":
        skala_celcius = (suhu - 32) * 5/9
    elif asal == "K":
        skala_celcius = (suhu - 273.15)

    #Celcius ke tujuan
    if tujuan == "C":
        return skala_celcius
    elif tujuan == "F":
        return (skala_celcius * 9/5 + 32)
    elif tujuan == "K":
        return (skala_celcius + 273.15)

def main_cuaca() -> None:
    print("=== Konversi Suhu ===")

    while True:
        input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ").lower()
        if input_suhu == "selesai":
            break

        skala_asal = input("Skala asal (C/F/K): ").upper()
        skala_tujuan = input("Skala tujuan (C/F/K): ").upper()

        try:
            suhu = float(input_suhu)
            hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
            print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")

        except ValueError:
            print("Error: Skala suhu tidak dikenali.")

main_cuaca()