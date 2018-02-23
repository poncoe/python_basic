# Membuat Deret menggunakan While

def deret(x,y):
    i = x+y
    while x<i:
        print(x,",",end="")
        x = x+1
    print()
    return
    
a = int(input("Masukan Bilangan 1 = "))
b = int(input("Masukan Bilangan 2 = "))
deret(a,b)
print()
deret(b,a)
