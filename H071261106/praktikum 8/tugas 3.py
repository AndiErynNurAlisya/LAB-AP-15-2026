import re


def bersihkan(nomor):
    # Hapus spasi dan tanda '-'
    return re.sub(r"[\s-]", "", nomor)


def validasi_telepon(nomor_bersih):
    # Hanya angka, panjang 10-13 digit
    return re.fullmatch(r"08\d{10,13}", nomor_bersih) is not None


print("=== Pembersihan Data Nomor Telepon ===\n")
jumlah = int(input("Masukkan jumlah data: "))
print()

data_awal = []
for i in range(1, jumlah + 1):
    data_awal.append(input(f"Nomor ke-{i}: "))
    print()

data_bersih = []
nomor_valid = []

print("--- Hasil Pembersihan ---\n")
for i, nomor in enumerate(data_awal, start=1):
    bersih = bersihkan(nomor)
    data_bersih.append(bersih)
    valid = validasi_telepon(bersih)

    if valid:
        nomor_valid.append(bersih)

    print(f"Data {i}:")
    print(f"Sebelum : {nomor}")
    print(f"Sesudah : {bersih}")
    print(f"Status  : {'Valid' if valid else 'Tidak valid'}\n")

print(f"Jumlah nomor valid: {len(nomor_valid)}")