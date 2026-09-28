N = int(input("masukkan jumlah baris kursi: "))
M = int(input("masukkan jumlah kursi: "))

print("--Setup Denah Bioskop NontonYuk--")

for i in range (1, N + 1):
    for j in range (1, M + 1):

        if j == 13:
            continue

        if i == 1:
            if j % 2 != 0:
                print(f"Baris {i} - Kursi {j}")

        else:
            print(f"Baris {i} - Kursi {j}")
