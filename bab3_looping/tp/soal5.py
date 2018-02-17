#program bintang

n = int(input("input n = "))
for i in range(n) :
    j=1
    while n+1-i > j :
        print("*",end=" ")
        j=j+1
        print()
