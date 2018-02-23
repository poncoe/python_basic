# Program Menentukan Sistostik Tekanan darah.

def tekanan_darah():
    lv1 = "Normal (Tidak Mengidap Hipertensi)"
    lv2 = "Prahipertensi"
    lv3 = "Hipertensi drajat 1"
    lv4 = "Hipertensi drajat 2"
    
    tekanan = int(input("Masukan Tekanan = "))
    if tekanan>=90 and tekanan<=119:
        print(lv1)
    elif tekanan>=120 and tekanan<=139:
        print(lv2)
    elif tekanan>=140 and tekanan<=159:
        print(lv3)
    elif tekanan>=160 :
        print(lv4)
    print(tekanan_darah())
tekanan_darah()
