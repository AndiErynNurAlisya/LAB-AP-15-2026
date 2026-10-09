def konversi_suhu(suhu, asal, tujuan):
    skala_valid = {'C', 'F', 'K'}
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")
    
    if asal == tujuan:
        return suhu
        
    if asal == 'C':
        celsius = suhu
    elif asal == 'F':
        celsius = (suhu - 32) * 5/9
    elif asal == 'K':
        celsius = suhu - 273.15  

    if tujuan == 'C':
        hasil = celsius
    elif tujuan == 'F':
        hasil = (celsius * 9/5) + 32
    elif tujuan == 'K':
        hasil = celsius + 273.15  

    return hasil

def main():
    print("--- Konversi Suhu ---")
    while True:
        input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
        
        if input_suhu.lower() == 'selesai':
            break
            
        try:
            suhu = float(input_suhu)
            asal = input("Skala asal (C/F/K): ").upper()
            tujuan = input("Skala tujuan (C/F/K): ").upper()
            
            hasil = konversi_suhu(suhu, asal, tujuan)
            
            print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")
            
        except ValueError as e:
            if str(e) == "Skala suhu tidak dikenali.":
                print("Error: Skala suhu tidak dikenali.")
            else:
                print("Error: Input suhu harus berupa angka.")
        except Exception:
            print("Error: Terjadi kesalahan pada sistem.")

if __name__ == "__main__":
    main()