str = ""
nilai = int(input("Masukan nilai = "))
while 0 <= nilai:
    hasil = nilai
    while hasil > 0:
        str = str + "*"
        hasil = hasil - 1
    str = str + "\n"
    nilai = nilai - 1
print()
print(str)
