def hitung_mundur(detik):
    if detik == 0:
        print("Luncurkan roket!")
        return
    
    print(f"T-minus: {detik}")
    
    hitung_mundur(detik - 1)

def main():
    print("=== PROGRAM HITUNG MUNDUR ROKET ===")
    
    waktu_awal = 5
    hitung_mundur(waktu_awal)

if __name__ == "__main__":
    main()








# def hitung_mundur(detik):
#     if detik == 0:
#         print("Luncurkan!")
#         return

#     print(detik)

#     hitung_mundur(detik - 1)

# def main():
#     waktu_awal = int(input("Masukkan angka awal hitunng mundur: "))
#     hitung_mundur(waktu_awal)

# if__name__ == "__main__"


















