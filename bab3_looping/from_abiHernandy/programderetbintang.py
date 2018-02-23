#Program bintang

n = int(input("Masukan n = "))
for i in range (n) :
    for j in range (n):
        if j < n-i :
            print("*", end = " ")
    print()
   
