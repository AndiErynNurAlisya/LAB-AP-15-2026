import re

def validasi_username(username):
    pola = r"^[a-zA-Z][a-zA-Z0-9_]{4,11}$"
    return bool(re.match(pola, username))

def main():
    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.")
    list_username = []
    
    while True:
        username = input("\nMasukkan username: ")
        if username == "SELESAI":
            break
            
        if validasi_username(username):
            print("Username tersedia.")
            list_username.append(username)
        else:
            print("Username tidak valid!")
            
    print("\n=== Rekapitulasi ===")
    print("Username valid:")
    for i, user in enumerate(list_username, 1):
        print(f"{i}. {user}")
    print(f"Jumlah username valid: {len(list_username)}")

main()