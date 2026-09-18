menu = ["kopi susu","matcha","americano"]
harga = [18000, 22000,15000]
jumlah = [4,3,5]

sub_kopi = harga [0] * jumlah[0]
sub_matcha = harga [1] * jumlah[1]
sub_americano = harga [2] * jumlah[2]

jumlah_barang = jumlah[0]+jumlah[1]+jumlah[2]

subtotal_pendapatan = [sub_kopi,sub_matcha,sub_americano]
total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000

pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

print(sub_kopi)
print(sub_matcha)
print(sub_americano)
print(subtotal_pendapatan)
print(pendapatan_bersih)
print(target_tercapai)
 
