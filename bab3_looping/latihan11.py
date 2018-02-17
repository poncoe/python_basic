# program bintang-bintang sejajar

n = int(input("masukan n = "))
for i in range(n) :
    for j in  range(n) :
        if j < n+i :
            print("*", end="")
    print()
