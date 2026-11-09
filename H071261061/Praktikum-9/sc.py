class Kendaraan:
    def __init__(self, merek, jenis):
        self.merek = merek
        self.jenis = jenis

    def info_kendaraan(self):
        return f"merek : {self.merek}, jenis : {self.jenis}"

    def klakson(self):
        return "Beep beep!"

mobil = Kendaraan("Avanza", "MPV")
print(mobil.info_kendaraan())
print(mobil.klakson())
print()

#========================================================================================

class Akun:
    def __init__(self, saldo_awal):
        self.awal = saldo_awal

    def get_saldo(self):
        return f"Sisa saldo: {self.awal}"

    def tarik(self, nominal):
        if self.awal >= nominal:
            self.awal -= nominal
            return f"Penarikan {nominal} berhasil"
        else:
            return "saldo tidak cukup" 

akun1 = Akun(100000)
print(akun1.tarik(40000))
print(akun1.get_saldo())
print()

#========================================================================================

class Pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self._gaji = gaji

    def get_info(self):

        return f"{self.nama} - Penghasilan: {self._gaji}"

class Manajer(Pegawai):
    def __init__(self, nama, gaji, bonus):
        super().__init__(nama, gaji)
        self.bonus = bonus

    def get_info(self):
        gaji_baru = self._gaji + self.bonus
        return f"{self.nama} - Penghasilan: {gaji_baru} (gaji {self._gaji} + bonus {self.bonus})"

org1 = Manajer("Hendra", 800000, 200000)
print(org1.get_info())