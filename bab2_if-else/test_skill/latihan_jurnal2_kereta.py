# Program Kereta Api

jarak = int(input("Masukan Jarak = "))
harga_tiket = int(input("Masukan Harga Tiket = "))

if (jarak>300) or (harga>500000) :
    beli = harga_tiket*0.5
elif (jarak>200) or (harga>300000) :
    beli = harga_tiket*0.8
else :
    beli = harga_tiket
    
print()
print("Harga Tiket = Rp", beli)
