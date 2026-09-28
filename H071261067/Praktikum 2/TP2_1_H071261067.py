#Tugas Praktikum 1
presentase_cabai = int(input("Masukan Presentase Tingkat Pedis Cabai: "))

#Level Pedas Cabai
if presentase_cabai >= 0 and presentase_cabai <= 10:
    print("Level Aman")
elif presentase_cabai >= 11 and presentase_cabai <= 40:
    print("Level Sedang")
elif presentase_cabai >= 41 and presentase_cabai <= 70:
    print("Level Pedas")
elif presentase_cabai >= 71:
    print("Level Ekstrem")

