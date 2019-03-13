#Latihan buat Sisa Siswa dan Bus yang akan di pakai di Suatu Bus Pariwisata

kapasitas = 25
jumlah_siswa = int(input("Jumlah Siswa = "))
bus = jumlah_siswa//kapasitas
sisa = jumlah_siswa%kapasitas
print("Bus yang akan digunakan = ", bus)
print("Sisa Siswanya adalah = ", sisa)
