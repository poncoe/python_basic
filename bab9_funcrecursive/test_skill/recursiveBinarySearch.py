# Recursive on Binnary Search

def binarySearch(mylist, item):
    if len(mylist) == 0:
        return False
    else:
        midpoint = len(mylist) // 2

    if mylist[midpoint] == item:
        return True
    else:
        if item < mylist[midpoint]:
            return binarySearch(mylist[:midpoint], item)
        else:
            return binarySearch(mylist[midpoint + 1:], item)


if __name__ == '__main__':
    j = []
    k = int(input("Enter length of your list: "))
    for i in range(k):
        l = int(input("element %s of your list: " % (i + 1)))
        j.append(l)
    j.sort()
    print(j)

    s = int(input("Find the number : "))
    print(binarySearch(j, s))
