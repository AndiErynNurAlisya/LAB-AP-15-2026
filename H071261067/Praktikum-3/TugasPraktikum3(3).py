#Tugas 3
while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))
        break
    except ValueError:
        print("Input jumlah kursi harus berupa angka")

print("\n---Sistem Reservasi PO BUS Dimulai---")

sisa_kursi = N
total_pendapatan = 0

while sisa_kursi > 0:
    print(f"\nSisa kursi : {sisa_kursi}")

    try:
        umur  = int(input("Masukkan umur penumpang: "))
    except ValueError:
        print("Umur harus berupa angka")
        continue
    if umur < 0:
        print("Umur tidak valid")
        continue
    elif umur <= 5:
        print("Kategori: Balita - Tiket Gratis (Rp 0)")
        harga_tiket = 0
    elif umur <= 12:
        print("Kategori : Anak - Harga: 50.000 ")
        harga_tiket = 50000
    else:
        print("Kategori : Dewasa - Harga : Rp 100.000")       
        harga_tiket = 100000 
    sisa_kursi -=1
    total_pendapatan += harga_tiket

print("---Semua Kursi Terisi---")
print(f"Total pendapatan perjalanan PO BUS kali ini : Rp {total_pendapatan} ")