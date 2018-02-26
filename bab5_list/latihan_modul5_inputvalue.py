# Membuat input nama menggunakan looping

loop_kalimat = int(input("Masukan Looping = "))
dict1={}
for i in range(loop_kalimat):
    print("Masukan Key ke",i+1,"= ",end="")
    key = input()
    print("Masukan isi Key ke",i+1,"= ",end="")
    isi = input()
    dict1[key]=isi
print(dict1)

