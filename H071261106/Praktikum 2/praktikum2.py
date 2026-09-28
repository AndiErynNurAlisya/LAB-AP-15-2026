jarak = int(input("Masukkan jarak pengiriman (KM): "))
express_input = input("Layanan express (Ya/Tidak).").capitalize()

if jarak < 5:
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
else:
    tarif = 35000

biaya_express = 15000 if express_input == "Ya" else 0

total = tarif + biaya_express

print("Total tarif pengiriman: Rp", total)