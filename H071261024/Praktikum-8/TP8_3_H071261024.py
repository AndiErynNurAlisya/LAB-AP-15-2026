import re

def main():
    print("=== Pembersihan Data Nomor Telepon ===")
    jumlah = int(input("\nMasukkan jumlah data: "))
    data_telepon = []
    
    for i in range(1, jumlah + 1):
        nomor = input(f"\nNomor ke-{i}: ")
        data_telepon.append(nomor)
        
    print("\n--- Hasil Pembersihan ---")
    valid_count = 0
    
    for i, nomor_sebelum in enumerate(data_telepon, 1):
        # menghapus karakter
        nomor_sesudah = re.sub(r'[\s-]', '', nomor_sebelum)
        
        if re.match(r'^\d{10,13}$', nomor_sesudah):
            status = "Valid"
            valid_count += 1
        else:
            status = "Tidak valid"
            
        print(f"Data {i}:")
        print(f"Sebelum: {nomor_sebelum}")
        print(f"Sesudah: {nomor_sesudah}")
        print(f"Status : {status}\n")
        
    print(f"Jumlah nomor valid: {valid_count}")


main()