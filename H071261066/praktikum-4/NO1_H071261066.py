def hitung_subtotal(harga, jumlah, adalah_member=False):
    sub_total = harga * jumlah

    if adalah_member:
        sub_total = sub_total * 0.9
    return int(sub_total)


def main():
    print("SELAMAT DATANG DI MINIMARKET")
    member = input("anda member? (y/n): ")

    if member == "y":
        is_member = True
    else:
        is_member = False

    total_belanja = 0

    while True:
        nama_barang = input("masukkan nama batang (kosongkan kalau udah): ")

        if nama_barang == "":
            break

        harga = int(input("harga barang: "))
        jumlah = int(input("jumlah barang: "))

        subtotal_belanja = hitung_subtotal(harga, jumlah, adalah_member=is_member)
        print(f"subtotal {nama_barang}: Rp{subtotal_belanja}")
        total_belanja += subtotal_belanja

    print(f"total belanja: {total_belanja}")
main()