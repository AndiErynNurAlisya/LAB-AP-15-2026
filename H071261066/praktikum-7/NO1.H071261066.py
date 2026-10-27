import os
from datetime import datetime

FOLDER_INVOICES = "Invoices"
if not os.path.exists(FOLDER_INVOICES):
    os.makedirs(FOLDER_INVOICES)

FILE_HISTORY = "trx_history.txt"

def generate_id_transaksi(nama_kasir):
    inisial = "".join([kata.upper() for kata in nama_kasir.split()[:3]])
    if len(inisial) < 3:
        inisial = nama_kasir[:3].upper()
    
    sekarang = datetime.now()
    thn = sekarang.strftime("%y")
    bln = sekarang.strftime("%m")
    tgl = sekarang.strftime("%d")
    jam_menit = sekarang.strftime("%H%M")
    angka_acak = sekarang.strftime("%f")[-3:]
    
    return f"{inisial}{thn}{bln}{tgl}{jam_menit}{angka_acak}"

def menu_buat_invoice(nama_kasir):
    id_transaksi = generate_id_transaksi(nama_kasir)
    waktu_str = datetime.now().strftime("%d/%m/%y %H:%M") 
    waktu_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    produk_list = []
    total_nominal = 0
    
    while True:
        nama_produk = input("Masukkan nama produk    : ")
        harga_produk = int(input("Masukkan harga produk   : "))
        jumlah_beli = int(input("Masukkan jumlah produk  : "))
        
        subtotal = harga_produk * jumlah_beli
        total_nominal += subtotal
        
        nama_display = nama_produk
        if len(nama_display) > 16:
            nama_display = nama_display[:13] + "..."

        produk_list.append({
            'nama': nama_display,
            'harga': harga_produk,
            'jumlah': jumlah_beli,
            'subtotal': subtotal
        })
        
        print("===============================================================")
        lanjut = input("Tambah produk? (y/t)    : ").lower()
        print("===============================================================")
        if lanjut != 'y':
            break
            
    isi_invoice = "===============================================================\n"
    isi_invoice += f"                           TOKO {nama_kasir.upper()}\n"
    isi_invoice += "===============================================================\n"
    isi_invoice += f"Nama kasir        : {nama_kasir}\n"
    isi_invoice += f"Waktu transaksi   : {waktu_str}\n"
    isi_invoice += "===============================================================\n"
    isi_invoice += "                          Daftar Produk                          \n"
    isi_invoice += "===============================================================\n"
    isi_invoice += f"| {'Nama':<15} | {'Harga':<11} | {'Jumlah':<6} | {'Total':<14} |\n"
    isi_invoice += "===============================================================\n"
    
    for p in produk_list:
        harga_format = f"Rp{p['harga']}"
        total_format = f"Rp{p['subtotal']}"
        isi_invoice += f"| {p['nama']:<15} | {harga_format:<11} | {p['jumlah']:<6} | {total_format:<14} |\n"
    isi_invoice += "===============================================================\n"
    total_akhir_format = f"Rp{total_nominal}"
    isi_invoice += f"| {'TOTAL':<15} | {'':<11} | {'':<6} | {total_akhir_format:<14} |\n"
    isi_invoice += "===============================================================\n\n"
    isi_invoice += "                  TERIMA KASIH TELAH BERBELANJA                \n"
    isi_invoice += "===============================================================\n"
    
    nama_file = os.path.join(FOLDER_INVOICES, f"{id_transaksi}.txt")
    with open(nama_file, "w") as f:
        f.write(isi_invoice)
        
    if not os.path.exists(FILE_HISTORY) or os.path.getsize(FILE_HISTORY) == 0:
        with open(FILE_HISTORY, "w") as f_hist:
            f_hist.write("==================================================================\n")
            f_hist.write(f"| {'Waktu':<19} | {'ID Transaksi':<15} | {'Nominal Transaksi':<22} |\n")
            f_hist.write("==================================================================\n")
            
    baris_riwayat = f"| {waktu_log} | {id_transaksi} | Rp. {total_nominal:<16} |\n"
    with open(FILE_HISTORY, "a") as f_hist:
        f_hist.write(baris_riwayat)
        f_hist.write("==================================================================\n")
        
    print("                      TRANSAKSI BERHASIL                         ")
    print("===============================================================")

def menu_cari_invoice():
    id_cari = input("Masukkan ID transaksi   : ").strip()
    nama_file = os.path.join(FOLDER_INVOICES, f"{id_cari}.txt")
    print("===============================================================")
    
    if os.path.exists(nama_file):
        with open(nama_file, "r") as f:
            print(f.read())
    else:
        print(f"Transaksi dengan ID {id_cari} tidak ditemukan.")
    print("===============================================================")

def main():
    print("===============================================================")
    print("                         SELAMAT DATANG                          ")
    print("===============================================================")
    nama_kasir = input("Masukkan nama kasir     : ").strip()
    print("===============================================================")
    
    while True:
        print("Pilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Keluar")
        print("===============================================================")
        pilihan = input("Masukkan opsi pilihan   : ")
        print("===============================================================")
        
        if pilihan == '1':
            menu_buat_invoice(nama_kasir)
        elif pilihan == '2':
            menu_cari_invoice()
        elif pilihan == '3':
            print("                           SAMPAI JUMPA                          ")
            print("===============================================================")
            break
        else:
            print("Pilihan opsi tidak valid.")
            print("===============================================================")

if __name__ == "__main__":
    main()