#Tugas Praktikum 2
jarak_pengiriman = int(input("Masukan Jarak Pengiriman Anda (Km): "))
layanan = input("Layanan express? (ya/tidak): ").lower()

#Biaya Pengiriman
if jarak_pengiriman < 5:
    tarif = 10000
elif jarak_pengiriman >= 5 and jarak_pengiriman <= 20:
    tarif = 20000
elif jarak_pengiriman > 20:
    tarif = 35000

layanan = 15000 if layanan == "ya" else 0
total_tarif = tarif + layanan
print("Total Tarif Pengiriman: Rp", total_tarif)

