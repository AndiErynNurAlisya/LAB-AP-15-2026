import os
import random
from datetime import datetime

def buat_folder_invoices():
    if not os.path.exists("invoices"):
        os.makedirs("invoices")

def buat_invoice(nama_kasir):
    buat_folder_invoices()
    
    inisial_kasir = "".join([kata[0].upper() for kata in nama_kasir.split()])[:3]
    if len(inisial_kasir) < 3:
        inisial_kasir = inisial_kasir.ljust(3, 'X')

    daftar_belanja = []
    total_harga = 0

    while True:
        print("=" * 65)
        nama_produk = input("Masukkan nama produk         : ").strip()
        try:
            harga_produk = float(input("Masukkan harga produk        : "))
            jumlah_produk = int(input("Masukkan jumlah produk       : "))
        except ValueError:
            print("Harga harus berupa angka dan jumlah harus berupa bilangan bulat!")
            continue

        subtotal = harga_produk * jumlah_produk
        total_harga += subtotal
        daftar_belanja.append({
            'nama': nama_produk,
            'harga': harga_produk,
            'jumlah': jumlah_produk,
            'subtotal': subtotal
        })

        print("=" * 65)
        tambah = input("Tambah produk? (y/t)         : ").strip().lower()
        if tambah != 'y':
            break

    if not daftar_belanja:
        print("Transaksi dibatalkan karena tidak ada produk yang dimasukkan.")
        return

    waktu_sekarang = datetime.now()
    thn = waktu_sekarang.strftime("%y")
    bln = waktu_sekarang.strftime("%m")
    tgl = waktu_sekarang.strftime("%d")
    jam_menit = waktu_sekarang.strftime("%H%M")
    
    angka_acak = str(random.randint(100, 999))

    id_transaksi = f"{inisial_kasir}{thn}{bln}{tgl}{jam_menit}{angka_acak}"
    nama_file = f"invoices/{id_transaksi}.txt"

    waktu_lengkap = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")
    
    isi_invoice = "=" * 45 + "\n"
    isi_invoice += f"{'STRUK BELANJA / INVOICE':^45}\n"
    isi_invoice += "=" * 45 + "\n"
    isi_invoice += f"ID Transaksi : {id_transaksi}\n"
    isi_invoice += f"Waktu        : {waktu_lengkap}\n"
    isi_invoice += f"Kasir        : {nama_kasir}\n"
    isi_invoice += "-" * 45 + "\n"
    isi_invoice += f"{'Produk':<18} | {'Qty':<3} | {'Subtotal':<15}\n"
    isi_invoice += "-" * 45 + "\n"
    
    for item in daftar_belanja:
        isi_invoice += f"{item['nama']:<18} | {item['jumlah']:<3} | Rp. {item['subtotal']:,.0f}\n"
    
    isi_invoice += "-" * 45 + "\n"
    isi_invoice += f"TOTAL PEMBAYARAN : Rp. {total_harga:,.0f}\n"
    isi_invoice += "=" * 45 + "\n"

    with open(nama_file, "w", encoding="utf-8") as f:
        f.write(isi_invoice)

    catat_riwayat(waktu_lengkap, id_transaksi, total_harga)

    print("=" * 65)
    print(f"{'TRANSAKSI BERHASIL':^65}")
    print("=" * 65)

def cari_invoice():
    print("=" * 65)
    id_trx = input("Masukkan ID Transaksi        : ").strip()
    nama_file = f"invoices/{id_trx}.txt"

    if os.path.exists(nama_file):
        print(f"\n--- Invoice ditemukan: {id_trx}.txt ---")
        with open(nama_file, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print(f"\nMaaf, invoice dengan ID '{id_trx}' tidak ditemukan di folder 'invoices'.")
    print("=" * 65)

def catat_riwayat(waktu, id_trx, nominal):
    file_riwayat = "trx_history.txt"
    file_exists = os.path.exists(file_riwayat)

    with open(file_riwayat, "a", encoding="utf-8") as f:
        if not file_exists:
            f.write("=" * 60 + "\n")
            f.write(f"| {'Waktu':<19} | {'ID Transaksi':<18} | {'Nominal Transaksi':<15} |\n")
            f.write("=" * 60 + "\n")
        
        f.write(f"| {waktu} | {id_trx} | Rp. {nominal:,.0f} |\n")

def tampilkan_riwayat():
    print("=" * 65)
    file_riwayat = "trx_history.txt"
    if os.path.exists(file_riwayat):
        with open(file_riwayat, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Belum ada riwayat transaksi yang tercatat.")
    print("=" * 65)

def main():
    print("=" * 65)
    print(f"{'SELAMAT DATANG':^65}")
    print("=" * 65)
    nama_kasir = input("Masukkan nama kasir          : ").strip()
    if not nama_kasir:
        nama_kasir = "Kasir"

    while True:
        print("=" * 65)
        print("Pilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Lihat Riwayat Transaksi") # Tambahan fitur riwayat sesuai soal 3
        print("4. Keluar")
        print("=" * 65)
        
        pilihan = input("Masukkan opsi pilihan        : ").strip()
        
        if pilihan == '1':
            buat_invoice(nama_kasir)
        elif pilihan == '2':
            cari_invoice()
        elif pilihan == '3':
            tampilkan_riwayat()
        elif pilihan == '4':
            print("=" * 65)
            print("Terima kasih telah menggunakan aplikasi kasir!")
            print("=" * 65)
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()