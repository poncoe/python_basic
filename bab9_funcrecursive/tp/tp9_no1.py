# Fungsi Rekursi untuk Menghitung Nilai Faktorial

n = int(input("Masukan Nilai N = "))
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else :
        return faktorial(n-1)*n

faktor = faktorial(n)
print("Hasilnya Faktorialnya = ",faktor)
