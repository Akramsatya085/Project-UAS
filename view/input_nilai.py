import Modul as m
def input_data():
    nama = str(input("nama\t\t: "))
    nim = str(input("nim\t\t: "))
    tugas =int(input("tugas\t\t: "))
    uts = int(input("uts\t\t: "))
    uas = int(input("uas\t\t: "))
    akhir = round(float(tugas * 0.30 + uts * 0.35 + uas * 0.35),2)
    m.Data [nama]=nama, nim, tugas, uts, uas, akhir
