# Program Faktorial

def faktorial(n, r):
    i = 1
    hasil = 1
    while i <= n :
        hasil = hasil*i
        i = i+1
    return hasil

def kombinasi(n,r):
    kombinasi = faktorial(n, r) / (faktorial(r, r) * faktorial(n, r))
    return kombinasi

n = int(input("Masukan Bilangan 1 = "))
r = int(input("Masukan Bilangan 2 = "))

hasil = kombinasi(n,r)
print("Hasil Kombinasinya Adalah = ",hasil)