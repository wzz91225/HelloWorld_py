#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def HeapSort():
    pass




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
