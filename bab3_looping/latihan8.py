# program deret diantara a dan b

a = int(input("masukan nilai a = "))
b = int(input("masukan nilai b = "))
if a > b :
    atas = a
    bawah = b
else :
    atas = b
    bawah = a
#endif
while bawah <= atas :
    print(bawah)
    bawah = bawah + 1
