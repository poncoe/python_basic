# Created by github @adnanhf

import json


def readFile():
    file = open('angka.txt')
    val = file.read()
    return val.split()
    file.close()


def parser(list):
    return [int(list[i]) for i in range(len(list))]


def writeFile(list):
    file = open('angkaurut.txt', 'w')
    json.dump(list, file)
    file.close()


def bubleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


def insertionSort(list):
    for i in range(len(list)):
        x, j = list[i], i - 1
        while j >= 0 and list[j] > x:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = x


if __name__ == '__main__':
    thelist = parser(readFile())
    '''
    choose one: Buble or Insertion
    '''
    # bubleSort(thelist)
    insertionSort(thelist)
    print(thelist)
    writeFile(thelist)