#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def BubbleSort(f):
    for i in range(len(f) - 1):
        for j in range(i + 1, len(f)):
            if f[i] > f[j]:
                temp = f[i]
                f[i] = f[j]
                f[j] = temp



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
BubbleSort(f)
OutputArr(f)
