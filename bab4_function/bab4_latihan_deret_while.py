# Membuat Deret menggunakan While

def deret(a,b):
    n = 1
    while n<b:
        print(a,",",end="")
        a = a + 1
        n = n + 1
    print(a,",",end="")
a = int(input("Masukan Bilangan 1 = "))
b = int(input("Masukan Bilangan 2 = "))
deret(a,b)
print()
deret(b,a)
