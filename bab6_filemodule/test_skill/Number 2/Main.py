# don't ever try to edit this files, unless you know what happen if you edit it
import os
import OpenFile
import TambahData
import HapusData
import viewData
import SimpanData
import Tampilan
import json

print("=============")
print("1. New File")
print("2. Open File")
print("=============")
pilih=int(input("Masukkan Pilihan : "))
if pilih == 1 :
    L = []
    nama = input("Masukkan nama File yg akan disimpan .txt : ")
elif pilih==2 :
    nama = input("Masukkan nama File .txt : ")
    L = OpenFile.Open(nama)

os.system("cls")
pil = Tampilan.tapil()
os.system("cls")
while pil != 5 :
    if pil == 1 :
        L = TambahData.tambah(L)
        print("enter untuk kembali ke menu")
        input()
    elif (pil==2):
        L = HapusData.Hapus(L)
        print("Data berhasil dihapus, enter untuk kembali menu")
        input()
    elif (pil==3):
        viewData.viewAll(L)
        print("enter untuk kembali ke menu")
        input()
    elif (pil==4):
        SimpanData.Simpan(L,nama)
        print("Data berhasil di simpan, enter untuk kembali ke menu")
        input()
    os.system("cls")
    pil=Tampilan.tapil()
    os.system("cls")