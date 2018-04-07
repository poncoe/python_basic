# Program Insertion Sort

i = 1
L = []
y = int(input("Masukan Banyaknya Looping = "))
while i <= y:
    print("Nilai", i, ":", end=" ")
    nilai = int(input(" "))
    i = i + 1
    L.append(nilai)

# Insertion Sort (Desc)
x = len(L)
for i in range(1,x):
    n = L[i]
    z = i-1
    while z >= 0 and L[z] < n:
        L[z+1] = L[z]
        z = z - 1
        L[z+1] = n
print("Nilai Terurut : ", L)

