# Latihan membuat alas segitiga

def luass(a,t):
    l = (a*t)/2
    return l

alas = int(input("Masukan Alas = "))
tinggi = int(input("Masukan Tinggi = "))

luas = luass(alas,tinggi)
#print(int(luas)) --> jika pengen di outputkan menggunakan integer
print(luas)
