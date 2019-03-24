# Searching Binnary Search

i = 1
L1 = []
L = []
n = int(input("Masuknnya Banyaknya List = "))
while i <=n:
    print("Masukan NIM = ",i,":",end=" ")
    nim = int(input(""))
    print("Masukan Nama = ",i,":",end=" ")
    nama = input("")
    i = i + 1
    L1 = [nim,nama]
    L.append(L1)

print()
print(L)
print()

# Searching

cari = int(input("Input NIM yang akan Dicari = "))
a = 0
b = len(L)-1
berhasil = False
L.sort()
while a<=b and not berhasil:
    mid = (a+b)//2
    for i in L:
        if L[mid][0]==cari:
            hasil = L[mid][1]
            berhasil = True
        else:
            if cari<L[mid][0]:
                a = mid+1
if berhasil:
    print("Nama Mahasiswa = ",hasil)
else :
    print("Tidak Ditemukan")
