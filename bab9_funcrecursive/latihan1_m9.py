# Latihan Rekursif

def jum(n):
    if (n == 0): # dimulai dari 0
        return 0 # dimulai dari 0
    elif (n == 1): # dimulai dari 1
        return 1 # dimulai dari 1
    else :
        return jum(n-1) + n

if __name__=="__main__":
    a = int(input("Masukan Nilai N = "))
    b = jum(a)
    print("outputnya adalah", b)

