# Fibbonaci Example

def fibbonaci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibbonaci(x - 1) + fibbonaci(x - 2)


if __name__ == '__main__':
    k = int(input("Enter the number : "))
    for i in range(k + 1):
        print(fibbonaci(i), end=" ")
