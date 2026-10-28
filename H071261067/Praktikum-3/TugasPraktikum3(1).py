
#Tugas 1
print("---Rekapitulasi Transaksi Dins Store--- ")
print("ketik '0' untuk menutup toko dan mengakhiri sesi.")

while True:
    try:
        item_input = input("Masukkan jumlah item : ")
        item = int(item_input)
    except ValueError:
        print("Input harus berupa angka!")
        continue
    if item == 0:
        print("Toko ditutup. Sesi rekap selesai")
        break
    elif item < 0:
        print("Jumlah tidak boleh negatif")
        continue
    elif item > 100:
        print("Maksimal 100 item per transaksi")
        continue
    else:
        print(f"Transaksi {item} item berhasi")

