# -*- coding: utf-8 -*-

import sys
import os.path


MAX_DISTANCE = sys.maxsize



def floyd():
    pass



def input_data():
    try:
        infile = open(os.path.join(sys.path[0], 'ShortestPath.in'), 'r')
        n = int(infile.readline())
        m = int(infile.readline())
        f = [[] for i in range(m)]
        for i in range(m):
            f[i] = [int(a) for a in infile.readline().split()]
        infile.close()
    except IOError:
        n = int(input())
        m = int(input())
        f = [[] for i in range(m)]
        for i in range(m):
            f[i] = [int(a) for a in input().split()]

    adjacent = [[int(MAX_DISTANCE) for j in range(n)] for i in range(n)]
    dis = [[int(MAX_DISTANCE) for j in range(n)] for i in range(n)]
    for i in range(n):
        adjacent[i][i] = 0
        dis[i][i] = 0
    for a, b, dis in f:
        adjacent[a][b] = dis




if __name__ == "__main__":
    input_data()
    
