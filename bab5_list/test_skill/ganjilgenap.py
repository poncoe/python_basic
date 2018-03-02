# Program Ganjil Genap

def ganjil(a,b):
    l1 = []
    l2 = []
    while a <= b:
        if a % 2 == 1:
            l2.append(a)
        l1.append(a)
        a = a+1
    print(l1)
    print(l2)

if __name__ == "__Main__":
    a = int(input("Masukan Bilangan 1 = "))
    b = int(input("Masukan Bilangan 2 = "))
    ganjil(a,b)