import Modul as m
def cetak_daftar():
    if m.Data.items():
        print("="* 84)
        print(f"|{'DATA MAHASISWA':^82}|")
        print("="* 84)
        print(f"|{'N0':^4}|{'NAMA':^20}|{'NIM':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")
        n = 0
        for i in m.Data.items():
            n += 1
            print(f"|{n:^4}|{i[1][0]:^20}|{i[1][1]:^20}|{i[1][2]:^10}|{i[1][3]:^6}|{i[1][4]:^6}|{i[1][5]:^10}|")
        print("="* 84)
    else:
        print("="* 84)
        print(f"|{'TIDAK ADA DATA':^82}|")
        print("="* 84)
def cetak_pencarian():
    cari = str(input('MASUKAN NAMA: '))
    if cari in m.Data.keys():
        print("="* 84)
        print(f"|{'DATA MAHASISWA':^82}|")
        print("="* 84)
        print(f"|{'N0':^4}|{'NAMA':^20}|{'NIM':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")
        n = 0
        for i in m.Data.items():
            n += 1
            print(f"|{n:^4}|{m.Data[cari][0]:^20}|{m.Data[cari][1]:^20}|{m.Data[cari][2]:^10}|{m.Data[cari][3]:^6}|{m.Data[cari][4]:^6}|{m.Data[cari][5]:^10}|")
        print("="* 84)
    else:
        print("="* 84)
        print(f"|{'TIDAK ADA DATA':^82}|")
        print("="* 84)