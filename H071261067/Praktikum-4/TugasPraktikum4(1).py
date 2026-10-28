# Tugas 1
def hitung_total_belanja(harga,jumlah, adalah_member=False):
    sub_total = harga * jumlah
    if adalah_member:
        sub_total = sub_total-(sub_total * 0.1)
        return int(sub_total)

def main():
    print("Selamat Datang di Kasir Minimarket Aribatus")

    input_member = input("Apakah anda member?(y/n): ")
    adalah_member = True if input_member == 'y' else False

    total_belanja = 0
    while True:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai):")

        if nama_barang == "":
            break

        harga = int(input("Harga barang: "))
        jumlah = int(input("Jumlah barang:"))

        sub_total = hitung_total_belanja(harga,jumlah, adalah_member)
        print(f"Sub total :{nama_barang} Rp: {sub_total}")

        total_belanja += sub_total
    print(f"Total belanja: {total_belanja}")
if __name__ == "__main__":
    main() 


# def hitung_total_belanja(harga, jumlah, adalah_member=False):
#     sub_total = harga * jumlah
#     if adalah_member:
#         sub_total = sub_total-(sub_total * 0.1)
#         return int(sub_total)

# def main():
#     print("Selamat datang di Kasir Minimarket!")
#     input_member = input("Apakah Anda member? (y/n): ")
#     adalah_member = True if input_member == "y" else False

#     total_belanja =  0
#     while True:
#         nama_barang = input("Masukkan nama  barang (kosongkan untuk selesai): ")

#         if nama_barang == "":
#             break

#         harga = int(input("Harga Barang: "))
#         jumlah = int(input("Jumlah barang: "))

#         sub_total = hitung_total_belanja(harga, jumlah, adalah_member)
#         print(f"Sub total {nama_barang}, Rp{sub_total}")

#         total_belanja += sub_total
#     print(f"Total belanja {total_belanja}")
# if __name__ == "__main__":
#     main()
