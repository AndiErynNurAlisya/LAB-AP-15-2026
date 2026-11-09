import re

def validasi_nim(nim):
    pattern = r"^H071\d{6}$"
    return bool(re.match(pattern, nim))

def validasi_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def validasi_telepon(telepon):
    pattern = r"^\d{10,13}$"
    return bool(re.match(pattern, telepon))


print("=== Validasi Data Mahasiswa ===")
nim = input("Masukkan NIM\t\t: ")
email = input("Masukkan Email\t\t: ")
telepon = input("Masukkan No. Telp\t: ")
    
status_nim = "Valid" if validasi_nim(nim) else "Tidak Valid"
status_email = "Valid" if validasi_email(email) else "Tidak Valid"
status_telepon = "Valid" if validasi_telepon(telepon) else "Tidak Valid"
    
print("\n--- Hasil Validasi ---")
print(f"NIM\t\t: {status_nim}")
print(f"Email\t\t: {status_email}")
print(f"No. Telepon\t: {status_telepon}")
    
if status_nim == "Valid" and status_email == "Valid" and status_telepon == "Valid":
    print("\nData mahasiswa berhasil diverifikasi!")
else:
    print("\nTerdapat data yang tidak valid.")
