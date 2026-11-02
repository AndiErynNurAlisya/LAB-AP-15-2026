import re

def validasi_nim(nim):
    pola = r"^H071\d{6}$"
    return bool(re.match(pola, nim))

def validasi_email(email):
    pola = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pola, email))

def validasi_telepon(telp):
    pola = r"^\d{10,13}$"
    return bool(re.match(pola, telp))

def main():
    print("=== Validasi Data Mahasiswa ===")
    nim = input("Masukkan NIM     : ")
    email = input("Masukkan Email   : ")
    telp = input("Masukkan No. Telp : ")
    
    status_nim = "Valid" if validasi_nim(nim) else "Tidak valid"
    status_email = "Valid" if validasi_email(email) else "Tidak valid"
    status_telp = "Valid" if validasi_telepon(telp) else "Tidak valid"
    
    print("\n--- Hasil Validasi ---")
    print(f"NIM        : {status_nim}")
    print(f"Email      : {status_email}")
    print(f"No. Telepon: {status_telp}")
    
    if status_nim == "Valid" and status_email == "Valid" and status_telp == "Valid":
        print("\nData mahasiswa berhasil diverifikasi!")

main()