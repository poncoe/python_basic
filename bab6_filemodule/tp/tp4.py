import json
coe=json.load(open("DAPno3.txt","r"))
data = ['NIM', 'Nama', 'Nilai UTS']
print(*data)
for i in coe:
    print(*i)
