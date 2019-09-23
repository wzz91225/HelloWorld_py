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
    f = [int(i) for i in input().split(" ")]

    # f = []
    # for i in input().split(" "):
    #     if isinstance(i, int) or isinstance(i, float):
    #         f.append(i)

    return f



def OutputArr(f):
    for i in range(len(f)):
        print(f[i])




f = InputArr()
BubbleSort(f)
OutputArr(f)
