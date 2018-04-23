# Triangle Recursive Pascal

def pascal(p, b):
    if p == 0:
        return 1
    elif p == b:
        return 1
    else:
        return pascal(p, b - 1) + pascal(p - 1, b - 1)


if __name__ == '__main__':
    n = int(input('Input sum of row: '))
    for i in range(n + 1):
        for j in range(i + 1):
            print(pascal(j, i), end=' ')
        print('')
