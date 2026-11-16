import re
def validasi_username(username):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,11}", username) is not None

daftar_valid = []

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.\n")

while True:
    username = input("Masukkan username: ")

    if username == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.\n")
        daftar_valid.append(username)
    else:
        print("Username tidak valid!\n")

print("\n=== Rekapitulasi ===")
print("Username valid:")
for i, nama in enumerate(daftar_valid, 1):
    print(f"{i}. {nama}")
print(f"\nJumlah username valid: {len(daftar_valid)}")