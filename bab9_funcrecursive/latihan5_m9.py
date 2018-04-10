# Latihan Rekursif Palindrom

def jum(n):
    if (n == 0): # dimulai dari 0
        return 0 # dimulai dari 0
    elif (n == 1): # dimulai dari 1
        return 1 # dimulai dari 1
    else :
        return jum(n-1) + n

def fibo(n):
    if (n==1) or (n==2):
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

def fak(n):
    if (n==0) or (n==1):
        return 1
    else :
        return n*fak(n-1)

def cetak(l,n):
    if n == 0:
        print(l[n])
    else:
        cetak(l, n-1)
        print(l[n])

        # dibalik

        print(l[n])
        cetak(l, n-1)

def polindrom(kata):
    if len(kata) < 1:
        return True
    else :
        if kata[0] == kata[len(kata)-1]:
            return polindrom(kata[1:len(kata)-1])
        else :
            return False
        

if __name__=="__main__":
    a = int(input("Masukan Nilai N = "))
    b = fibo(a)
  
    d = fak(a)
    l = [4,7,3,8,4,8,5]
    print()
    print("outputnya penjumlahan", c)
    print("fibonacinya adalah", b)
    print("ouput Faktorial dari",a, "adalah", d)
    cetak(l,a)

# Bagian Palindrom

    kata = input("Masukan Kata = ")
    if palindrom(kata) :
        print("Palindrom")
    else :
        print("Tidak Palindrom")
