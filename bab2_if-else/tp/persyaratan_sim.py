#Program Persyaratan SIM

umur = int(input("Masukan Umur Anda = "))
nilai = int(input("Masukan Nilai Tes Anda = "))
lulus = "Selamat Anda Berhak Mendapatkan Sim Anda"
gagal = "Maaf, Anda tidak berhak mendapatkan sim anda\nSilahkan Coba lagi Bulan atau tahun Depan"

if(umur>17) :
    if(nilai<60) :
        print()
        print(gagal)
    else :
        print()
        print(lulus)
        
else :
        print()
        print(gagal)
