jarak = float(input("masukkan jarak pengiriman(km) : "))
layanan_expres = input("apakah kamu berlayanan expres(ya/tidak) : ")

if jarak < 5:
   tarif_pengiriman = 10000
elif 5 <= jarak <= 20:
   tarif_pengiriman = 20000
else:
   tarif_pengiriman = 35000

biaya_tambahan = 15000 if layanan_expres == "ya" else 0
total_tarif_pengiriman = tarif_pengiriman + biaya_tambahan

print(f"total tarif pengiriman anda adalah: Rp{total_tarif_pengiriman}")



    
