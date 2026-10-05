def subtotal_harga(harga: int, jumlah: int, adalah_member: bool = False) -> int:
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = int(subtotal * 0.9)
    return subtotal

def main_kasir() -> None:
    print("Selamat datang di Kasir Minimarket!")
    status = input("Apakah Anda member? (y/n): ").lower()

    if status == "y":
        member = True
    else:
        member = False

    total = 0

    while True:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        if nama_barang == "":
            break

        harga = int(input("Harga barang: "))
        jumlah = int(input("Jumlah barang: "))

        hasil = subtotal_harga(harga, jumlah, adalah_member=member)
        print(f"Subtotal {nama_barang}: Rp{hasil}")

        total += hasil
    print(f"Total belanja: Rp{total}")

main_kasir()
