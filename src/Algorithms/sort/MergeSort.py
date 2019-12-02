# -*- coding: utf-8 -*-



def MergeArr(f, left, middle, right):
    temp = [None] * len(f)
    i = left
    j = middle + 1
    k = left

    while (i <= middle and j <= right):
        if f[i] < f[j]:
            temp[k] = f[i]
            i += 1
        else:
            temp[k] = f[j]
            j += 1
        k += 1
    
    while (i <= middle):
        temp[k] = f[i]
        i += 1
        k += 1

    while (j <= right):
        temp[k] = f[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        f[i] = temp[i]



def MergeSort(f, left, right):
    middle = (left + right) >> 1
    if left < middle:
        MergeSort(f, left, middle)
    if middle + 1 < right:
        MergeSort(f, middle + 1, right)
    MergeArr(f, left, middle, right)




def InputArr():
    try:
        infile = open('sort.in', 'r')
        f = [int(i) for i in infile.read().split()]
        infile.close()
    except IOError:
        f = [int(i) for i in input().split()]
    
    return f



def OutputArr(f):
    try:
        outfile = open('sort.out', 'w')
        for i in range(len(f) - 1):
            outfile.write(str(f[i]) + ' ')
        outfile.write(str(f[-1]))
        outfile.close()
    except IOError:
        for i in range(len(f)):
            print(f[i])



f = InputArr()
MergeSort(f, 0, len(f) - 1)
OutputArr(f)
