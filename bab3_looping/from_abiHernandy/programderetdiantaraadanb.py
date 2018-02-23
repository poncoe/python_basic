a = int(input("Masukan a = "))
b = int(input("Masukan b = "))
if a > b :
    atas = a
    bawah = b
else :
    atas = b
    bawah = a
while bawah <= atas :
    print(bawah)
    bawah = bawah + 1
