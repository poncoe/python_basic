# Procedure Rekursif mencetak bilangan L(n) sampai L(0)

import json

f = open("list.txt", "r+")
x = json.load(f)

n = int(input("Masukan Nilai N = "))
def ily(n,x):
    if n == 0:
        print(x[0])
    else :
        print(x[n],end=" ")
        ily(n-1, x)

ily(n,x)
