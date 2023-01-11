import view as v 
import Modul as m
Data={}
def tambah_data(): 
    print ("TAMBAH_DATA")
    v.input_data()
    print("DATA BERHASIL DI TAMBAHKAN")
def ubah_data():
    print ("UBAH_DATA")
    cari = str(input("MASUKAN NAMA: "))
    if cari in m.Data.keys():
        v.input_data()
        print("DATA BERHASIL DI UBAH")

    else: 
        print("DATA TIDAK DITEMUKAN")
def hapus_data():
    print ("HAPUS_DATA")
    cari = str(input("MASUKAN NAMA: "))
    if cari in m.Data.keys():
        del m.Data[cari]
        print("DATA BERHASIL DI HAPUS")

    else: 
        print("DATA TIDAK DITEMUKAN")
    
def cari_data():
   print ("CARI DATA") 
   v.cetak_pencarian