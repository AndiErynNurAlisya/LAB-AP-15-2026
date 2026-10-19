#Tugas 2
print("---Setup Denah Bioskop NontonYuk")

while True:
    try:
        baris = input("Masukkan jumlah baris: ")
        N = int(baris)
        if N < 0:
            print("Jumlah baris harus lebih dari 0")
        else:
            break
    except ValueError:
        print("Jumlah baris harus berupa angka")

while True:
    try:
        kursi = input("Masukkan jumlah kursi per baris: ")
        M = int(kursi)
        if M < 0:
            print("Jumlah kursi harus lebih dari 0")
        else:
            break
    except ValueError:
        print("Jumlah kursi harus berupa angka")

print("---Daftar Kursi Tersedia---")

for baris in range(1, N + 1):
    for kursi in range(1, M + 1):
        if kursi == 13:
            continue
        if baris == 1 and kursi % 2 == 0:
            continue
        print(f"Baris {baris} - Kursi {kursi}")