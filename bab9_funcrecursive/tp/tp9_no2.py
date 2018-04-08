# Fungsi Rekursif untuk menghitung jumlah nilai F(x) dengan X

n = int(input("Masukan Nilai X = "))
def f(n):
    if n == 1:
        return 1
    elif n>1:
        return f(n-1)+n
    else :
        return ""

hsl = f(n)
print("x = ",hsl)
