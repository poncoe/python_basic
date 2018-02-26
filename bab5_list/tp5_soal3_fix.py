# Membuat Looping pada List

n = int(input("Masukan n = "))
i = 1
L = []
while i<=n :
    #h = input("kata : ")
 #   L.insert(i-1,i)#h) # h dipake buat input dari kata
    L.insert(i-1,n-i+1) #buat reversi angka
    i=i+1
#L.reverse() # buat fungsi reversi angka
print(L)
hasil = sum(L) #kalo pake string ini gapake
print(hasil) #kalo pake string ini gapake
