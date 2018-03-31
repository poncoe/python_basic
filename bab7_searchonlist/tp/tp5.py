# Tp No 5 Linear Search

looping = int(input("Input Looping Mahasiswa = "))
L = []
i = 0

while i < looping :
    nim = int(input("Masukan NIM Anda = "))
    nama = input("Masukan Nama Anda = ")
    coe = [nim,nama]
    L.append(coe)
    i = i + 1

print()
print(L)

def linearSearch(x,y):
    for i in range(len(x)):
        if x[i][1] == y :
            z = x[i][0]
    return z

print()
cari = input("Input Nama yang anda dicari = ")
print()
print("NIM Mahasiswa : ",linearSearch(L,cari))
