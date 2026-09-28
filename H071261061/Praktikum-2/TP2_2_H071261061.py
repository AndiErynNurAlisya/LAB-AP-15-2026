#no.2
jarak = float(input("Masukkan Jarak Pengiriman : "))
layanan = input("Layanan Ekspress (ya/tidak) : ")
harga = 0


if 0 < jarak < 5:
    harga = 10000
elif 5 <= jarak <= 20 :
    harga = 20000
elif jarak > 20:
    harga = 35000


ekspres = harga + 15000 if layanan == "ya" else harga
print(ekspres)