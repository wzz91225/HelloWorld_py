# -*- coding: utf-8 -*-

import sys
import os.path



def InsertSort(f):
    for i in range(1, len(f)):
        for j in range(0, i):
            if (f[j] > f[i]):
                temp = f[i]
                for k in range(i - 1, j - 1, -1):
                    f[k + 1] = f[k]
                f[j] = temp
                break



def InputArr():
    try:
        infile = open(os.path.join(sys.path[0], 'sort.in'), 'r')
        f = [int(i) for i in infile.read().split()]
        infile.close()
    except IOError:
        f = [int(i) for i in input().split()]

    return f



def OutputArr(f):
    try:
        outfile = open(os.path.join(sys.path[0], 'sort.out'), 'w')
        for i in range(len(f) - 1):
            outfile.write(str(f[i]) + ' ')
        outfile.write(str(f[-1]))
        outfile.close()
    except IOError:
        for i in range(len(f)):
            print(f[i])



if __name__ == "__main__":
    f = InputArr()
    InsertSort(f)
    OutputArr(f)
