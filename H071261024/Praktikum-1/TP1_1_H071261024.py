menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3,5]

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

barang_terjual = sum(jumlah)
target_tercapai = (total_seluruh > 200000) and (barang_terjual > 10)

print("--- LAPORAN PENJUALAN KOPI SENJA ---")
print(f"Subtotal {menu[0]}: Rp{subtotal_pendapatan[0]:,}")
print(f"Subtotal {menu[1]}: Rp{subtotal_pendapatan[1]:,}")
print(f"Subtotal {menu[2]}: Rp{subtotal_pendapatan[2]:,}")
print(f"Pendapatan Bersih : Rp{pendapatan_bersih:,}")
print(f"Hasil Target : {target_tercapai}")