umur = int(input("umur : "))
nilaites = int(input("nilaites : "))
if umur > 17:
    if nilaites > 80:
        hasil = ("Selamat anda berhak mendapatkan SIM")
    else:
        hasil = ("Maaf anda tidak berhak mendapatkan SIM, Nilai test anda kurang")
elif umur == 17:
    if nilaites > 80:
        hasil = ("Maaf anda tidak berhak mendapatkan SIM, umur anda belum mencukupi")
    elif nilaites < 80:
        hasil = ("Maaf anda tidak berhak mendapatkan SIM, umur dan nilai belum mencukupi")
elif umur < 17:
    if nilaites < 80:
        hasil = ("maaf anda tidak lulus karena nilai dan umur tidak mencukupi")
print(hasil)
