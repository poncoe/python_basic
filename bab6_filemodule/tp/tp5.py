import json
import modultp5
coe = json.load(open("DAPno3.txt","r"))
data = ['NIM','Nama','Nilai UTS']
print(data[0],"\t"+data[1]+"\t"+data[2])
for i in coe:
    for t in i:
        print(t, end="\t")
    print("")
print("rata-rata utsnya adalah", modultp5.ratarata(data))
