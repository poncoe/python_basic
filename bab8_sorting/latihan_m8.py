L=[["Roronoa Zoro", 320],["Monkey D Luffy", 500],["Nico Robin", 130],["Nami", 66],["Sanji", 177]]
print(L)
n=len(L)
for i in range (1,n):
    x=L[i]
    j=i-1
    while j>=0 and L[j][1] < x[1]:
        L[j+1] = L[j]
        j=j-1
    L[j+1]=x





