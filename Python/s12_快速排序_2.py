def quiec_sort(alist):
    if len(alist) < 2:
        return alist
    else:
        pivot = alist[0]
        less = [i for i in alist[1:] if i <= pivot]
        greater = [i for i in alist[1:] if i > pivot]
        return quiec_sort(less) + [pivot] + quiec_sort(greater)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 21, 44, 55, 20]
    print(li)
    nlist = quiec_sort(li)
    print(nlist)
