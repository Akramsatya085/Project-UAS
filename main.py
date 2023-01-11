import Modul as m
import view as v
import os



print("="*20)
print("|PROGRAM INPUT DATA|")
print("="*20)

while True: 
    print()
    menu = input("[(T)ambah, (L)ihat, (C)ari, (H)apus, (U)bah, (K)eluar] : ")
    print("~"*78)
    print()
    os.system("cls")

    if menu.lower() == 't':
        m.tambah_data()

    elif menu.lower() == "l":
        v.cetak_daftar()

    elif menu.lower() == 'c':
        m.cari_data()
        v.cetak_pencarian()

    elif menu.lower() == "h":
        m.hapus_data()

    elif menu.lower() == "u":
       m.ubah_data()

    elif menu.lower() == "k":
        print("Program selesai, Terima Kasih :) ")
        break

    else:
        print("\n INPUT {} TIDAK ADA!, Silakan pilih [T/L/I/H/U/K] untuk menjalankan program!".format(menu))