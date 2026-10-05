def hitung_mundur(angka: int) -> None:
    if angka == 0:
        print("0")
        print("Luncurkan!")
        return

    print(angka)
    hitung_mundur(angka - 1)

def main_peluncuran() -> None:
    while True:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))
        if angka_awal < 0:
            print("Input tidak valid, angka tidak boleh negatif!")
        else:
            hitung_mundur(angka_awal)
            break

main_peluncuran()