# Program Bubble Sort

i = 1
L = []
y = int(input("Masukan Banyaknya Looping = "))
while i <= y:
    print("Nilai", i, ":", end=" ")
    nilai = int(input(" "))
    i = i + 1
    L.append(nilai)
print("Inputan Nilai", L)

#Buble Sort
x = len(L)
for i in range(x):
    for y in range(x-i-1):
        if L[y] > L[y+1]:
            pindah = L[y]
            L[y] = L[y+1]
            L[y+1] = pindah

#Median
if (y%2==0):
    bmedian = x / 2 -1
    bmedianyo = int(bmedian)
    hasil=[L[bmedianyo], L[bmedianyo+1]]
else:
    bmedian = (y +1) / 2 - 1
    bmedianyo = int(bmedian)
    hasil = [L[bmedianyo]]

print("Sorting : ", L)
print("Minimum : ", min(L))
print("Maximum : ", max(L))
print("Median : ", hasil)
