# Program Mencari Bilangan Terbesar dan Terkecil

bil1 = int(input("Masukan Bilangan 1 = "))
bil2 = int(input("Masukan Bilangan 2 = "))
bil3 = int(input("Masukan Bilangan 3 = "))

#Nilai Terbesar

if (bil1>bil2) and (bil1>bil3) :
    print()
    print("Terbesarnya adalah = ", bil1)
elif (bil2>bil1) and (bil2>bil3) :
    print()
    print("Terbesarnya adalah = ", bil2)
else :
    print()
    print("Terbesarnya yaitu = ", bil3)

#Nilai Terkecil
    

if (bil1<bil2) and (bil1<bil3) :
    print("Terkecilnya adalah = ", bil1)
elif (bil2<bil1) and (bil2<bil3) :
    print("Terkecilnya adalah = ", bil2)
else :
    print("Terkecilnya yaitu = ", bil3)
