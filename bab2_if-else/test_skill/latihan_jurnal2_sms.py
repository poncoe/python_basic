# Program REG SMS

reg = input("Ketik SMS = ")

if (reg[0:4] == "REG ") :
    print("Selamat anda terdaftar sebagai", reg[4:len(reg)])
else :
    print("Maaf Format anda Salah")
