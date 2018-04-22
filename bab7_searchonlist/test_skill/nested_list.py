# Created by github @adnanhf

def seqSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if (alist[pos][0]).lower() == item.lower():
            found = True
        else:
            pos += 1

    if found:
        print('Menu found!\nName : %s, price : Rp%s,00' % (alist[pos][0], alist[pos][1]))
    else:
        print('Menu not found!')


if __name__ == '__main__':
    menu = [['Ayam Goreng', 12000], ['Kol Goreng', 5000], ['Mie', 7000], ['Telor', 5000], ['Pecel Lele', 14000]]
    z = input('Input menu you want to know : ')
    seqSearch(menu, z)
