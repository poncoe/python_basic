import json

dict1 = []
for i in range(2):
    print("Masukan NIM",i+1,"= ",end="")
    nim = int(input())
    print("Masukan Nama",i+1,"= ",end="")
    nama = input()
    print("Masukan Nilai UTS",i+1,"= ",end="")
    nilai = int(input())
    vue = [nim,nama,nilai]
    dict1.append(vue)
coe = open("DAPno3.txt", "w")
coe.write(json.dumps([dict1]));
coe.close()
