# Program Bintang-Bintang Gajelas

nilai = int(input("Masukan Nilai = "))
for i in range(nilai+1) :
    for j in range(i):
        print("*",end="")
    print()
for i in range(nilai):
    j=1
    while j < nilai-i:
        print("*",end="")
        j=j+1
    print()
