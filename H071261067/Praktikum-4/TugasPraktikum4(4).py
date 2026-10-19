def konversi_suhu(nilai, dari_skala, ke_skala):
    skala_valid = ['C', 'F', 'K']
    if dari_skala.upper() not in skala_valid or ke_skala.upper() not in skala_valid:
        raise ValueError("Skala suhu tidak valid! Harap gunakan 'C', 'F', atau 'K'.")
    
    if dari_skala == 'C':
        celsius = nilai
    elif dari_skala == 'F':
        celsius = (nilai - 32) * 5 / 9
    elif dari_skala == 'K':
        celsius = nilai - 273.15
        
    if ke_skala == 'C':
        return celsius
    elif ke_skala == 'F':
        return (celsius * 9 / 5) + 32
    elif ke_skala == 'K':
        return celsius + 273.15

def main():
    print("=== Konversi suhu===")
    
    try:
        nilai = float(input("Masukkan suhu (atau 'selesai' untuk keluar): "))
        dari_skala = input("Skala awal (C/F/K): ").upper()
        ke_skala = input("Skala tujuan (C/F/K): ").upper()
        
        hasil = konversi_suhu(nilai, dari_skala, ke_skala)
        print(f"Hasil: {nilai} {dari_skala} = {hasil:.2f} {ke_skala}")
        
    except ValueError as e:
        print(f"Peringatan Error: {e}")

if __name__ == "__main__":
    main()





