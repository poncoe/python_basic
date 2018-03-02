# Membuat aplikasi Orde 2x2 dan Mencari Determinan

loop_nilai = 4
a = []
for i in range (loop_nilai):
    input_nilai = int(input("Input Matriks = "))
    a.append(input_nilai)
print(a[0:2])
print(a[2:4])
determinan = a[0]*a[3]-a[1]*a[2]
print("Determinan A adalah =",determinan)
