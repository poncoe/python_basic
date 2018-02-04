umur = int(input("umur :"))
if (umur>17) :
    nilai = int(input("nilai tes :"))
    if (nilai>80):
            hasil=("Selamat")
    else :
            hasil=("Maaf")
else :
    hasil=("GAGAL")
print(hasil)