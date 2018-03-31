# TP No 4 Binnary Search

i = 1
L1 = []
L = []
n = int(input("Input Banyaknya List = "))
while i<=n :
    print("Masukan NIM Anda",i,":",end=" ")
    nim = int(input(""))
    print("Masukan Nama Anda",i,":",end=" ")
    nama = input("")
    i = i+1
    L1 = [nim,nama]
    L.append(L1)

print()
print(L)

print()
cari = int(input("Input NIM yang anda cari = "))
a = 0
b = len(L)-1
berhasil = False
L.sort()
while a<=b and not berhasil:
    mid=(a+b)//2
    for i in L :
        if L[mid][0]==cari:
            hasil = L[mid][1]
            berhasil = True
        else:
            if cari<L[mid][0]:
                a = mid+1
if berhasil:
    print("Nama Mahasiswa = ",hasil)
else:
    print("NIM Tidak Berhasil Ditemukan!")
