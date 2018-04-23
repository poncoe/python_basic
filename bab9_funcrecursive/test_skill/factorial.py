# Find Factorial Value

def factorial(x):
    if (x == 0):
        return 1
    else:
        return (x * factorial(x - 1))


def Combination(n, r):
    if r < 0:
        return 'rasio cannot be negative'
    else:
        return factorial(n) // (factorial(r) * factorial(n - r))


if __name__ == '__main__':
    n = int(input("n= "))
    r = int(input("r= "))
    print(Combination(n, r))
