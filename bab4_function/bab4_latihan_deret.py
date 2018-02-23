# Membuat Program Menampilkan Deret

def deret(bil1,bil2):
    i = bil1
    n = bil2
    j = bil1
    for i in range (bil2):
        print(bil1,",",end="")
        bil1 = bil1+1
    print()
    for n in range (j):
        print(bil2,",",end="")
        bil2 = bil2+1

bil1 = int(input("Masukan Bilangan 1 = "))
bil2 = int(input("Masukan Bilangan 2 = "))
deret(bil1,bil2)
