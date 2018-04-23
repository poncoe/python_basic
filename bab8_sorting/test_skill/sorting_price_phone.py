def bubleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j][1] > list[j + 1][1]:
                list[j], list[j + 1] = list[j + 1], list[j]


if __name__ == '__main__':
    thelist = [
              ['Nokia 3', 1235], ['iPhone 4', 2245],
              ['Nokia 5', 1250], ['iPhone 5', 6750],
              ['Nokia 6', 4500], ['iPhone 6', 1755],
              ['Nokia 8', 2395]]

    bubleSort(thelist)
    for i in range(len(thelist)):
        print('%s \tRp%s,00' % (thelist[i][0], thelist[i][1]))