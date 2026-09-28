menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000] 
jumlah = [4, 3, 5]

#no.1
sub_kopi = jumlah[0] * harga[0]
sub_matcha = jumlah[1] * harga[1]
sub_americano = jumlah[2] * harga[2]

#no.2
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

#no.3
total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

#no.4
total_barang = sum(jumlah)
target_tercapai = total_seluruh > 200000 and total_barang > 10

#input
print("subtotal pendapatan : ", subtotal_pendapatan)
print("total pendapatan : ", total_seluruh)
print("pendapatan bersih : ", pendapatan_bersih)
print("total barang : ", total_barang)
print("target tercapai : ", target_tercapai)