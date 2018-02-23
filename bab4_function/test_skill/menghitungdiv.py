# Program Menghitung DIV

def getDivMod(bil1,bil2,operator):
    if operator == "modulo":
        hasil = bil1 % bil2
    elif operator == "division":
        hasil = bil1 // bil2
    else:
        hasil = "Operator Salah"
    return hasil

def intro():
    intro = "Hi, Selamat Datang, Jika Masukan Operatornya 'Modulo' yaitu Mod dan 'Division' yaitu Div"
    print()
    print(intro)


intro()
print()

bil1 = int(input("Masukan Bilangan 1 = "))
bil2 = int(input("Masukan Bilangan 2 = "))
operator = input("Masukan Opeator = ")
print(getDivMod(bil1,bil2,operator))