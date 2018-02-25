# Program Mengimputkan nilai 1 sampai N dan Menghitung Jumlahnya

isi_list = []
nilai = int(input("Masukan Nilai N = "))
b = 1
hasil = 0
for i in range(nilai):
    isi_list.append(i+1)
while b <= nilai:
    hasil = hasil+b
    b = 1+b
hasil = sum(isi_list)
print("isi list =",isi_list)
print("Jumlah Isi List =",hasil)
