# Buatlah program untuk mencari suatu nilai integer dari list yang isinya diinputkan
# oleh user menggunakan fungsi binary search dan menampilkan nilai tersebut apabila data ada di dalam list.

# Created by github @adnanhf

def binarySearch(alist, item):
    alist.sort()
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if alist[middle] == item:
            found = True
        else:
            if item < alist[middle]:
                last = middle - 1
            else:
                first = middle + 1

    if found:
        print('Item found : ', item)
    else:
        print("Item not found!")


if __name__ == '__main__':
    thelist = []
    n = int(input('Input the amount of list elements : '))
    for i in range(n):
        element = int(input('Input the %s elements : ' % i + 1))
        thelist.append(element)
    x = int(input('Input the item you want to search : '))
    binarySearch(thelist, x)
