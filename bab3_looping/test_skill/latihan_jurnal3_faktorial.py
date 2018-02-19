# Program Menghitung Faktorial

nilai = int(input("Masukan Nilai = "))
if (nilai==0):
    hasil = 1
else:
    i=1
    hasil=1
    while(i <= nilai):
        hasil=hasil*i
        i=i+1
    print("Hasil =",hasil)
