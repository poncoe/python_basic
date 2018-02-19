# Program Bilangan Ganjil Pertama

nilai = int(input("Masukan Nilai N = "))
hasil = 0
i = 0
j = 0

while (i !=nilai) :
    j=j+1
    if (j%2 == 1):
        i = i+1
        hasil = hasil+j
print("hasilnya", hasil)
    
