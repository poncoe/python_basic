# Buble Sort & Insertion Sort

# Insertion Sort

i = 1
L = []
y = int(input("Masukin Banyak Looping = "))
while i <= y:
    print("Nilai",i,":",end=" ")
    nilai = int(input(" "))
    i = i + 1
    L.append(nilai)
print("Inputan Nilai",L)

### Implementasi Insertion Sort
##
##x = len(L)
##for i in range(1,x):
##    n = L[i]
##    z = i - 1
##    while z >=0 and L[z] < n:
##        L[z+1] = L[z]
##        z = z - 1
##        L[z+1] = n
##print("Nilai Terurut = ",L)

#Buble Sort

x = len(L)
for i in range(x):
    for y in range(x-i-1):
        if L[y] > L[y+1]:
            pindah = L[y]
            L[y] = L[y+1]
            L[y+1] = pindah

if (y%2==0):
    bmedian = x / 2 -1
    bmendianyo = int(bmedian)
    hasil = [L[bmendianyo], L[bmendianyo+1]]
else :
    bmendianyo = (y+1) / 2 - 1
    bmendianyo = int(bmedian)
    hasil = [L[bmendianyo]]

print("Sort =",L)
print("MIN = ",min(L))
print("MAX = ",max(L))
print("Median = ",hasil)
