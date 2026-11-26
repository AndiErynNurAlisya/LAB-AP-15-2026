def hitung_subtotal(harga, jumlah, is_member=False):
    subtotal = harga * jumlah

    if is_member:
        subtotal = subtotal * 90 // 100

    return subtotal


print("Selamat datang di Kasir Minimarket!")

status = input("Apakah Anda member? (y/n): ").lower()

if status == "y":
    is_member = True
else:
    is_member = False

total = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, is_member)

    print(f"Subtotal {nama_barang}: Rp{subtotal}")

    total += subtotal

print(f"Total belanja: Rp{total}")