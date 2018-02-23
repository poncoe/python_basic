#program deret bintang

n = int(input("Masukan n = "))
for i in range (n+1) :
    for j in range (i) :
        print("*", end = " ")
    print()
