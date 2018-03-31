L = []
n = int(input("Masukan Looping = "))

for i in range(n):
    a = input("Masukan Nama Makanan = ")
    b = int(input("Masukan Harga Makanan = "))
    c = [a,b]
    L.append(c)

print()
print(L)
print()
i = 0
j = 0

cari = input("Cari Makanan = ")
print()

while i<len(L) and j== 0:
    if L [i][0]== 0:
        j = [i][1]
    else :
        i = i + 1
if j == 0:
    print("Gaditemukan")
else :
    ("Ditemukan, yaitu nama makanan ", cari, "harganya ",j)
