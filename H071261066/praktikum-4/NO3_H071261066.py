def hitung_mundur(n):
    if n == 0:
        print(0)
        print("Luncurkan!")
    else:
        print(n)
        hitung_mundur(n - 1)

def main():
    while True:
        angka_input = input("Masukkan angka awal hitung mundur: ")
        
        angka = int(angka_input)
        
        if angka < 0:
            print("Input tidak valid, angka tidak boleh negatif.")
            continue
        else:
            hitung_mundur(angka)
            break

if __name__ == "__main__":
    main()