coe = open("DAP.txt", "r+")
vue = coe.read()
i=0
for index,item in enumerate(vue):
    if item==" ":
        pass
    else:
        i=i+1
k=1
while k<i:
    coe.write("\nDAP Sangat Mudah")
    k=k+1
coe.close()

