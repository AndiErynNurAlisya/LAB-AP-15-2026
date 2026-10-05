# Minta user memasukkan angka menu
pilihan = int(input("Masukkan nomor menu (1-3): "))

match pilihan:
    case 1:
        print("Kamu memilih Kopi Susu")
    case 2:
        print("Kamu memilih Matcha Latte")
    case 3:
        print("Kamu memilih Americano")
    case _:
        print("Nomor menu tidak valid!")