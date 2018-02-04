umur = int(input("umur :"))
nilai = int(input("nilai tes :"))
if (umur>17) :
    if (nilai>80):
            hasil=("Selamat")
    else :
            hasil=("Maaf")
else :
    hasil=("GAGAL")
print(hasil)