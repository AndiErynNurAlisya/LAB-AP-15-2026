from datetime import datetime
import random
import os

folder_saat_ini = os.path.dirname(os.path.abspath(__file__))
folder_invoices = os.path.join(folder_saat_ini, "invoices")
file_history = os.path.join(folder_saat_ini, "trx_history.txt")
os.makedirs(folder_invoices, exist_ok=True)

# Membuat header tabel di trx_history.txt jika file belum ada
if not os.path.exists(file_history):
    with open(file_history, "w") as f:
        border_hist = "=" * 90
        header_title = "|" + "RIWAYAT TRANSAKSI".center(88) + "|"
        header_col = "|" + "Waktu".center(19) + "|" + "ID Transaksi".center(25) + "|" + "Nominal Transaksi".center(40) + "|"
        f.write(border_hist + "\n")
        f.write(header_title + "\n")
        f.write(border_hist + "\n")
        f.write(header_col + "\n")
        f.write(border_hist + "\n")

def membuat_invoices(kasir, data_produk):
    waktu_sekarang = datetime.now().strftime("%Y%m%d%H%M%S")
    id_nama = kasir[:3].upper()
    id_tahun = waktu_sekarang[2:4]
    id_bulan = waktu_sekarang[4:6]
    id_tanggal = waktu_sekarang[6:8]
    id_jam_menit = waktu_sekarang[8:12]
    angka_random = random.randint(100, 999)
    
    id_transaksi = f"{id_nama}{id_tahun}{id_bulan}{id_tanggal}{id_jam_menit}{angka_random}"
    waktu_tampil = f"{id_tanggal}/{id_bulan}/{id_tahun} {waktu_sekarang[8:10]}:{waktu_sekarang[10:12]}"
    
    border = "=" * 79
    border1 = "|" + "Nama".center(38) + "|" + "Harga".center(14) + "|" + "Jumlah".center(8) + "|" + "Total".center(14) + "|"
    total_keseluruhan = 0
    total_item = 0
    
    nama_file = f"{id_transaksi}.txt"
    file_dalam_folder = os.path.join(folder_invoices, nama_file)
    
    # 1. Menulis file invoice (.txt)
    with open(file_dalam_folder, "w") as o:
        o.write(f"TOKO {kasir.capitalize()}".center(100))
        o.write("\n")
        o.write("=" * 100)
        o.write("\nNama kasir".ljust(20) + f": {kasir}")
        o.write(f"\nWaktu transaksi".ljust(20) + f": {waktu_tampil}")
        o.write("\n")
        o.write("=" * 100)
        o.write("\n\n")
        o.write("Daftar Produk".center(100))
        o.write("\n\n" + border.center(100))
        o.write("\n" + border1.center(100))
        o.write("\n" + border.center(100))
        
        for i in data_produk:
            total_item = i["Harga"] * i["Jumlah"]
            hasil = "| " + f"{i['Nama']}".ljust(37) + "|" + f"Rp{i['Harga']}".rjust(13) + " |" + f"{i['Jumlah']}".center(8) + "|" + f"Rp{total_item}".rjust(13) + " |"
            o.write("\n" + hasil.center(100))
            total_keseluruhan += total_item
            
        border_total = "|" + "TOTAL".center(38) + "|".rjust(25) + f"Rp{total_keseluruhan}".rjust(13) + " |"
        o.write("\n" + border.center(100))
        o.write("\n" + border_total.center(100))
        o.write("\n" + border.center(100))
        o.write("\n\n")
        o.write("=" * 100)
        o.write("\n" + "TERIMAKASIH TELAH BELANJA".center(100))
        o.write("\n")
        o.write("=" * 100 + "\n")
        
    # 2. Mencatat ke trx_history.txt dengan format tabel yang diminta
    with open(file_history, "a") as isi:
        baris_history = f"| {waktu_tampil.center(19)} | {id_transaksi.center(25)} | Rp{str(total_keseluruhan).rjust(37)} |"
        border_hist = "=" * 90
        isi.write(baris_history + "\n")
        isi.write(border_hist + "\n")
        
    print("=" * 54)
    print("TRANSAKSI BERHASIL".center(54))
    print("=" * 54)

# Program Utama
print("=" * 54)
print("SELAMAT DATANG".center(54))
print("=" * 54)
nama_kasir = input("Masukkan nama kasir".ljust(35) + ": ")

while True:
    print("=" * 54)
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print("=" * 54)
    pilih_opsi = input("Masukkan opsi pilihan".ljust(35) + ": ")
    print("=" * 54)
    
    if pilih_opsi == "1":
        data_list = []
        while True:
            try:
                nama_produk = input("Masukkan nama produk".ljust(35) + ": ")
                harga_produk = int(input("Masukkan harga produk".ljust(35) + ": "))
                jumlah_produk = int(input("Masukkan jumlah produk".ljust(35) + ": "))
                
                data = {
                    "Nama": nama_produk,
                    "Harga": harga_produk,
                    "Jumlah": jumlah_produk,
                }
                data_list.append(data)
                
                while True:
                    print("=" * 54)
                    tambah_produk = input("Tambah produk? (y/t)".ljust(35) + ": ")
                    print("=" * 54)
                    if tambah_produk == "y":
                        break
                    elif tambah_produk == "t":
                        membuat_invoices(nama_kasir, data_list)
                        break
                    else:
                        print("Input yang anda masukkan tidak valid")
                        continue
                if tambah_produk == "t":
                    break
            except ValueError:
                print("Harga atau jumlah yang anda masukkan tidak valid")
                continue
                
    elif pilih_opsi == "2":
        id_transaksi = input("Masukkan ID transaksi".ljust(35) + ": ")
        lokasi_file_folder = os.path.join(folder_invoices, id_transaksi + ".txt")
        
        if os.path.isfile(lokasi_file_folder):
            with open(lokasi_file_folder, "r") as ada:
                isi = ada.read()
                print("=== ISI FILE ===")
                print(isi)
        else:
            print(f"File '{id_transaksi}' tidak ditemukan.")
            
    elif pilih_opsi == "3":
        print("Terima kasih!")
        break
    else:
        print("Opsi yang anda pilih tidak valid!")