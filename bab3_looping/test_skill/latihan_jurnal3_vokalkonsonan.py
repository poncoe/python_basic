#Program Menentukan Vokal & Konsonan

kata = input("Masukan Kalimat = ")
vokal = 0
konsonan = 0
for i in range(len(kata)):
    if ((kata[i] == "a")or (kata[i] == "i")
        or (kata[i] == "u")or (kata[i] == "e")
        or (kata[i] == "o")or (kata[i] == "A")
        or (kata[i] == "I") or (kata[i] == "U")
        or (kata[i] == "E") or (kata[i] == "O")) :
                vokal = vokal +1
    elif(kata[i]==" "):
        pass
    else:
        konsonan = konsonan+1
print("Banyak Vokal : ",vokal)
print("Banyak Konsonan : ",konsonan)
