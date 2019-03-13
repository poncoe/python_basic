# r = baca file / read file
# r+ = baca & tulis file / read & write
# w = nulis file / write file
# w+ = nulis dan baca file / read & write
# JSON = Javascript ON

##coe = open("file.txt", "w")
##coe.write("Python sangat Mudah")
##coe.close()

##coe = open("file.txt", "r+")
##vue = coe.read()
##i = 0
##
##for index,item in enumerate(vue):
##    if item == " ":
##        pass
##    else:
##        i = i + 1
##k = 1
##while k<i:
##    coe.write("\nPython Sangat Mudah")
##    k = k + 1
##coe.close()

import json

##dict1 = []
##for i in range(2):
##    print("Masukan NIM",i+1,"= ",end="")
##    nim = int(input())
##    print("Masukan Nama",i+1,"= ",end="")
##    nama = input()
##    print("Masukan Nilai UTS",i+1,"= ",end="")
##    nilai = int(input())
##    vue = [nama,nim,nilai]
##    dict1.append(vue)
##coe = open("mahasiswa.txt", "w")
##coe.write(json.dumps([dict1]));
##coe.close()

coe = json.load(open("mahasiswa.txt", "r"))
data = ['NIM', 'Nama', 'Nilai UTS']
print(*data)
for i in coe:
    print(*i)
