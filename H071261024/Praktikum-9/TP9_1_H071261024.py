class Pemain:
    def __init__(self, nama, id_pemain, role, kill, assist, objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.kill = kill
        self.assist = assist
        self.objective = objective

    def hitung_skor_akhir(self):
        return (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)

    def status_performa(self):
        skor = self.hitung_skor_akhir()
        if skor >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

def tampilkan_data():
    print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
    jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))

    daftar_pemain = []

    for i in range(1, jumlah_pemain + 1):
        print(f"\n-- Data Pemain ke-{i} --")
        nama = input("Nama: ")
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")
        kill = float(input("Nilai Kill: "))
        assist = float(input("Nilai Assist: "))
        objective = float(input("Nilai Objective: "))

        pemain = Pemain(nama, id_pemain, role, kill, assist, objective)
        daftar_pemain.append(pemain)

    print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
    garis = "=" * 78
    print(garis)
    print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<11} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<15} |")
    print(garis)

    for i, p in enumerate(daftar_pemain, 1):
        skor = p.hitung_skor_akhir()
        status = p.status_performa()
        print(f"| {i:<3} | {p.nama:<10} | {p.id_pemain:<11} | {p.role:<10} | {skor:<10} | {status:<15} |")

    print(garis)

tampilkan_data()