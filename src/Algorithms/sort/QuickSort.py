#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def QuickSort(f, left, right):
    ll, rr = left, right
    pd = True

    while ll < rr:
        if f[ll] > f[rr]:
            temp = f[ll]
            f[ll] = f[rr]
            f[rr] = temp
            pd = not pd
        if pd:
            rr -= 1
        else:
            ll += 1
    
    if (ll - 1 > left):
        QuickSort(f, left, ll - 1)
    if (rr + 1 < right):
        QuickSort(f, rr + 1, right)




def InputArr():
    try:
        infile = open('sort.in', 'r')
        f = [int(i) for i in infile.read().split(" ")]
        infile.close()
    except IOError:
        f = [int(i) for i in input().split(" ")]

    # f = []
    # for i in input().split(" "):
    #     if isinstance(i, int) or isinstance(i, float):
    #         f.append(i)

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
QuickSort(f, 0, len(f) - 1)
OutputArr(f)
