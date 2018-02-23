# Program Menghitung Suhu

def reamur(nilai_suhu):
    reamur = nilai_suhu*0.8
    return reamur

def farenheit(nilai_suhu):
    farenheit = (nilai_suhu*1.8)+32
    return farenheit

def kelvin(nilai_suhu):
    kelvin = nilai_suhu+273
    return kelvin

def konversi(nilai_suhu):
    print("Hasil Suhu dari Reamur adalah = ",reamur(nilai_suhu),"R")
    print("Hasil Suhu dari Farenheit adalah = ", farenheit(nilai_suhu),"F")
    print("Hasil Suhu dari Kelvin adalah = ", kelvin(nilai_suhu),"K")

nilai_suhu = int(input("Masukan Suhu = "))
print()
konversi(nilai_suhu)