##Latihan args kwargs awokawok
# def hitung_pesanan(nama_pemesan, *harga_minuman, **detail_pesanan):
#     total=0
#     print(f"Pesanan atas nama: {nama_pemesan}")
#     for tot in harga_minuman:
#         total+=tot
#     print(f"Total harga: Rp {total}")

#     print("Detail Pesanan:")
#     for k, v in detail_pesanan.items():
#         print(f"- {k}: {v}")

#     return total

# hitung_pesanan("Haechan", 15000, 18000, 12000, meja=5, catatan="Less sugar")

##Latihan 2, pakai if-else

# def hitung_transaksi(nama_pembeli,*harga_barang,**opsi_tambahan):
#     print("=== NOTA TRANSAKSI ===")
#     print(f"Pembeli: {nama_pembeli}")

#     total = 0
#     for t in harga_barang:
#         total+=t
#     print(f"Totak Barang: Rp {total}")

#     diskon = 0
#     if "diskon" in opsi_tambahan:
#         diskon = opsi_tambahan["diskon"]
#         print(f"Diskon: Rp {diskon}")

#     ongkir = 0
#     if "ongkir" in opsi_tambahan:
#         ongkir = opsi_tambahan["ongkir"]
#         print(f"Ongkir: Rp {ongkir}")

#     print("-"*30)

#     total_akhir = total - diskon + ongkir
#     print(f"Total Akhir: Rp {total_akhir}")

#     return total_akhir

# total1 = hitung_transaksi("coky buccu", 50000, 75000, 100000, diskon=20000, ongkir=10000)

# print("\n" + "="*30 + "\n")

# total2 = hitung_transaksi("Kiki", 80000, 120000, ongkir=10000)

##Latihan 3-lambda
# keranjang = [
#     {"produk": "Kemeja", "harga": 150000, "jumlah": 2},
#     {"produk": "Stokot", "harga": 15000, "jumlah": 5},
#     {"produk": "Sepatu", "harga": 450000, "jumlah": 1},
#     {"produk": "Topi", "harga": 35000, "jumlah": 3},
#     {"produk": "Jaket", "harga": 250000, "jumlah": 2}
# ]

# produk_mahal = list(filter(lambda item: item["harga"] * item["jumlah"] > 100000, keranjang))
# hasil_akhir = sorted(produk_mahal, key=lambda item: item["jumlah"], reverse=True) #supaya dari besar-kecil
# print(hasil_akhir)

## Rekursi
# def pangkat_rekursif(basis, eksponen):
#     if eksponen == 0:
#         return 1
    
#     return basis * pangkat_rekursif(basis, eksponen - 1)
# pass

# print(pangkat_rekursif(2, 3))  
# print(pangkat_rekursif(5, 2)) 

## raise
# def validasi_pin(pin: str):
#     if len(pin) != 6:
#         raise ValueError("PIN harus terdiri dari tepat 6 digit angka!")
#     print("PIN valid!")


# # Memanggil fungsi di dalam try-except
# try:
#     validasi_pin("123")  # Hanya 3 digit
# except ValueError as e:
#     # 'e' menampung pesan string yang kita tulis di dalam raise di atas
#     print(f"❌ Terjadi kesalahan: {e}")

# # studi case 1 (coba-coba)
# # Tulis fungsi beli_pulsa di sini lengkap dengan Type Hinting, Docstring, Positional-Only, dan Keyword-Only
# def beli_pulsa(nomor_hp: str, /, nominal: int, *, metode_bayar: str = "Saldo Utama" ) -> str:
#     """Membeli pulsa untuk nomor HP yang ditentukan.

#     Args:
#         nomor_hp (str): Nomor HP tujuan pembelian pulsa.
#         nominal (int): Nominal pulsa yang ingin dibeli (minimal 10000).
#         metode_bayar (str, optional): Metode pembayaran yang digunakan. Defaults to "Saldo Utama".

#     Returns:
#         str: Pesan konfirmasi transaksi berhasil.

#     Raises:
#         ValueError: Jika panjang nomor HP tidak 10-13 digit, atau nominal < 10000.
#     """
#     # 1. Validasi nomor HP
#     if len(nomor_hp) < 10 or len(nomor_hp) > 13:
#         raise ValueError("Nomor HP harus terdiri dari 10-13 digit.")
#     # 2. Validasi nominal
#     if nominal < 10000:
#         raise ValueError("Minimal pembelian pulsa adalah Rp10.000.")
#     # 3. Return pesan sukses
#     return f"Berhasil membeli pulsa {nominal} ke {nomor_hp} via {metode_bayar}."



# # --- UJI COBA PROGRAM ---
# try:
#     # Coba panggil fungsi dengan berbagai skenario di sini
#     hasil = beli_pulsa("081234567890", 25000, metode_bayar="Bonus Poin")
#     print(f"✅ {hasil}")

# except ValueError as e:
#     print(f"❌ Transaksi Gagal: {e}")

# def luas_persegi_panjang(panjang, lebar):
#     return panjang * lebar
# luas = luas_persegi_panjang(5, 3)
# print(f"luas persegi panjang: {luas}")

# def ucapan_ulang_tahun(nama):
#     print(f"Selamat ulang tahun, {nama}! Semoga panjang umur.")

# ucapan_ulang_tahun("Rina")

# def sapa_pelanggan(nama, bahasa="Indonesia"):
#    if bahasa == "Indonesia":
#       print(f"Selamat datang, {nama!}")
#     else:
#       print("Dinda")

# def buat_profil(nama, umur, kota):
#     print(f"Nama: {nama}, Umur: {umur}, Kota: {kota}")

# buat_profil(umur="19", kota="Makassar", nama="Kiki")

# def cetak_biodata(**data):
#     for key, value in data.items():
#         print(f"{key}: {value}")

# cetak_biodata(nama="Andi", jurusan="Sistem Informasi", angkatan=2023)

# def tampilkan_data(*args, **kwargs):
#     print("Data:")
#     for data in args:
#         print(data)
#     print("Informasi Tambahan:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# tampilkan_data("Alice", "Bob", "Carol", pekerjaan="Pengajar", kota="Jakarta")

# def hitung_diskon(harga, /, *, persen=10):
#     potongan = harga * persen/100
#     return harga - potongan

# print(hitung_diskon(100000))

# tambah = lambda a, b: a + b
# print(tambah(2, 4))


# data = [("Andi", 20), ("Budi", 17), ("Citra", 25)]
# data_terurut = sorted(data, key=lambda x: x[1], reverse=True)
# print(data_terurut)

# def jumlah_hingga(n):
#     if n == 1:
#         return 1
#     else:
#         return n + jumlah_hingga(n-1)

# print(jumlah_hingga(5))


# def celcius_ke_faahrenheit(celcius: float) -> float:
#     return celcius * (9/5) + 32

# print(celcius_ke_faahrenheit(30.0))

# def cekUmur(umur):
#     if umur < 0:
#         raise ValueError("Umur tidak boleh bernilai negatif!")
#     return f"Umur valid: {umur}"

# print(cekUmur(20)) 
# print(cekUmur(-5)) 

# def luas(r):
#     return (22/7) * r**2
# print(luas(3))

# def keliling(d):
#     return  (22/7) * d
# print(keliling(3))



