def bubleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j][1] > list[j + 1][1]:
                list[j], list[j + 1] = list[j + 1], list[j]


if __name__ == '__main__':
    thelist = [
              ['Redmi 5A', 1235], ['Mi Note 3', 2245],
              ['Redmi Note 5A', 1250], ['Mi Mix 2', 6750],
              ['Redmi 5 Pro', 4500], ['Redmi Note 4x', 1755],
              ['Redmi 5 Plus', 2395]]

    bubleSort(thelist)
    for i in range(len(thelist)):
        print('%s \tRp%s,00' % (thelist[i][0], thelist[i][1]))