import re

def bersihkan(nomor):
    return re.sub(r"[ -]", "", nomor)

def validasi_telepon(nomor):
    return re.fullmatch(r"\d{10,13}", nomor) is not None

print("=== Pembersihan Data Nomor Telepon ===\n")
jumlah = int(input("Masukkan jumlah data: "))

data_awal = []
data_bersih = []
nomor_valid = []

for i in range(1, jumlah + 1):
    nomor = input(f"\nNomor ke-{i}: ")
    data_awal.append(nomor)
    data_bersih.append(bersihkan(nomor))

print("\n--- Hasil Pembersihan ---")
for i in range(jumlah):
    valid = validasi_telepon(data_bersih[i])
    if valid:
        nomor_valid.append(data_bersih[i])

    print(f"\nData {i + 1}:")
    print("Sebelum :", data_awal[i])
    print("Sesudah :", data_bersih[i])
    print("Status  :", "Valid" if valid else "Tidak valid")

print(f"\nJumlah nomor valid: {len(nomor_valid)}")