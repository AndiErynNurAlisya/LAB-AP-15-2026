class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        return "Perlu Evaluasi"

    def tampilkan_data(self, nomor):
        skor = self.hitung_skor_akhir()
        print(f"| {nomor:<3} | {self.nama:<10} | {self.id_pemain:<11} | "
              f"{self.role:<9} | {skor:<10.2f} | {self.status_performa():<14} |")


print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===\n")
jumlah = int(input("Masukkan jumlah pemain: "))

daftar_pemain = []

for i in range(1, jumlah + 1):
    print(f"\n-- Data Pemain ke-{i} --")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    nilai_kill = int(input("Nilai Kill: "))
    nilai_assist = int(input("Nilai Assist: "))
    nilai_objective = int(input("Nilai Objective: "))

    daftar_pemain.append(Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective))

garis = "=" * 76

print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print(garis)
print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<11} | {'Role':<9} | {'Skor Akhir':<10} | {'Status':<14} |")
print(garis)

for nomor, pemain in enumerate(daftar_pemain, 1):
    pemain.tampilkan_data(nomor)

print(garis)