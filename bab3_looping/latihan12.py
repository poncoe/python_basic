# program bintang-bintang naik turun

n = int(input("masukan n = "))
for i in range(n) :
    for j in  range(i) :
        if j < n-i :
            print("*", end="")
    print()
