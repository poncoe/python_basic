# Insertion sort, created by github @adnanhf

def insertionSort(list):
    for i in range(len(list)):
        x, j = list[i], i - 1
        while j >= 0 and list[j] < x:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = x


def sequentialSearch(list, item):
    pos = 0
    found = False

    while pos < len(list) and not found:
        if list[pos] == item:
            found = True
        else:
            pos += 1
    if found:
        print('the number you are looking for is at %s' % (pos + 1))
    else:
        print('the number you are looking for is not found!')


if __name__ == '__main__':
    thelist, n = [], int(input('Input the amount of list elements : '))
    for i in range(n):
        element = int(input('Input the %s elements : ' % (i + 1)))
        thelist.append(element)
    insertionSort(thelist)
    find = int(input('Input the number you want to search: '))
    print(thelist)
    sequentialSearch(thelist, find)