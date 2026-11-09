class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objetive):
        self.nama = nama
        self.idpemain = id_pemain
        self.role = role
        self.kill = nilai_kill
        self.asist = nilai_assist
        self.objtv = nilai_objetive

    def hitung_skor_akhir(self):
        skor_akhir = (0.3*self.kill) + (0.3*self.asist) + (0.4*self.objtv)
        return skor_akhir

    def status_performa(self):
        skor_akhir = self.hitung_skor_akhir()
        if skor_akhir >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(pemain):
        print("=== REKAPITULASI PERFORMA PEMAIN ===")
        print("="*79)
        print("| No   | Nama       | ID Pemain  | Role       | Skor Akhir  | Status           |")
        print("="*79)
        for i, data in enumerate(pemain, 1):
            print(f"| {i}   | {data["nama"]:<11}| {data["id"]:^11}| {data["role"]:<11}| {data["skor"]:<12}| {data["status"]:<17}|")
        print("="*79)

datapemain = []
print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===\n")

berapa = int(input("Masukkan jumlah pemain: "))
print()

for i in range(1, berapa + 1):
    print(f"-- Data Pemain Ke-{i} --")
    nama = input("Nama: ")
    Id = input("ID Pemain: ")
    role = input("Role: ")
    kill = int(input("Nilai Kill: "))
    asist = int(input("Nilai Assist: "))
    objektiv = int(input("Nilai Objective: "))
    print()
    pemain = Pemain(nama, Id, role, kill, asist, objektiv)
    skor = pemain.hitung_skor_akhir()
    status = pemain.status_performa()
    data = {
        "nama":nama,
        "id": Id,
        "role": role,
        "skor": skor,
        "status": status
    }
    datapemain.append(data)

Pemain.tampilkan_data(datapemain)


        