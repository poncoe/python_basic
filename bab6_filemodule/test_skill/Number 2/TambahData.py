# adding data record into list 'L'
def tambah(L):
    print("Masukkan NIM\t\t: ", end="")
    a = input()
    print("Masukkan Nama\t\t: ", end="")
    b = input()
    print("Masukkan nilai UTS\t: ", end="")
    c = int(input())
    # Lanjutkan Dibawah
    record=[a,b,c]
    L.append(record)
    return L