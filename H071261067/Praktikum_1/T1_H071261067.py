menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah [2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

jumlah_barang = sum(jumlah)
target_tercapai = (total_seluruh > 200000 and jumlah_barang > 10)

print("Sub Total Kopi : Rp", sub_kopi)
print("Sub Total Matcha Latte: Rp", sub_matcha)
print("Sub Total Americano: Rp", sub_americano)
print(subtotal_pendapatan)
print("Pendapatan Bersih: Rp", pendapatan_bersih)
print(target_tercapai)


