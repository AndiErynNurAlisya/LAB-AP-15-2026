import re


print("=== Pembersihan Data Nomor Telepon ===")
jumlah_data = int(input("Masukkan jumlah data: "))
    
daftar_sebelum = []
daftar_sesudah = []
daftar_status = []
jumlah_valid = 0
    
for i in range(1, jumlah_data + 1):
    nomor = input(f"Nomor ke-{i}: ")
    daftar_sebelum.append(nomor)
        
    bersih = re.sub(r"[\s-]", "", nomor)
    daftar_sesudah.append(bersih)
        
    if re.match(r"^\d{10,13}$", bersih):
        daftar_status.append("Valid")
        jumlah_valid += 1
    else:
        daftar_status.append("Tidak valid")
            
print("\n--- Hasil Pembersihan ---")
for i in range(jumlah_data):
    print(f"Data {i + 1}:")
    print(f"Sebelum: {daftar_sebelum[i]}")
    print(f"Sesudah: {daftar_sesudah[i]}")
    print(f"Status : {daftar_status[i]}\n")
        
print(f"Jumlah nomor valid: {jumlah_valid}")
