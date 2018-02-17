# Program Menentukan Index Nilai

nilai = int(input("Masukan Nilai = "))

if (nilai>80) :
    index = "A"
elif (nilai<=80) and (nilai>65) :
    index = "B"
elif (nilai<=65) and (nilai>60) :
    index = "C"
else :
    index = "D"
print("anda mendapatkan index =", index)
