n=int(input("Jumlah isi list"))
i=1
L=[]
while i <= n:
    a=int(input())
    L.append(a)
    i=i+1
print(L)

n=len(L)
for i in range (1,n):
    x=L[i]
    j=i-1
    while j>=0 and L[j] < x:
        L[j+1] = L[j]
        j=j-1
    L[j+1]=x

bo=False
g=0
while g<= n-1:
    if L[g]%2==0:
        g=g+1
    else:
        hsl=L[g]
        g=n
        bo=True
if bo:
    print("Ganjil Terbesar :", hsl)
else:
    print("Yaah gaada")
