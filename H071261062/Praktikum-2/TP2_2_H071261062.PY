jarak = int(input("Masukkan jarak pengiriman (km) : "))

if jarak < 0:
    print("Input tidak vaid")
else:
    layanan = input("Layanan express (ya/tidak) : ")
    if jarak < 5:
        jarak = 10000
    elif jarak <= 20:
        jarak = 20000
    else:
        jarak = 35000
    express = 15000 if layanan == "ya" else 0
    tarif = jarak + express
    print (f"Total tarif pengiriman: Rp{tarif}")