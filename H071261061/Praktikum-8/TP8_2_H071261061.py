import re

def validasi_username(username):
    # Panjang 5-12 karakter, hanya huruf/angka/underscore, diawali huruf, tanpa spasi
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]{4,11}$"
    return bool(re.match(pattern, username))


print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")
    
username_valid = []
    
while True:
    user_input = input("Masukkan username: ")
    if user_input == "SELESAI":
        break
            
    if validasi_username(user_input):
        print("Username tersedia.")
        username_valid.append(user_input)
    else:
        print("Username tidak valid!")
            
print("\n=== Rekapitulasi ===")
print("Username valid:")
for i, uname in enumerate(username_valid, 1):
    print(f"{i}. {uname}")
print(f"Jumlah username valid: {len(username_valid)}")
