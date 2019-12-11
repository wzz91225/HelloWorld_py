# -*- coding: utf-8 -*-

import sys
import os.path



class Graph():
    def __init__(self):
        try:
            infile = open(os.path.join(sys.path[0], 'bfsa.in'), 'r')
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
        
        self.n = n
        self.adjacent = [[0 for j in range(n)] for i in range(n)]
        for x, y in f:
            self.adjacent[x][y] = 1
            self.adjacent[y][x] = 1


    
    def shortest_BFS(self, begin, end):
        if begin == end:
            return 0
        dis = [-1 for i in range(self.n)]
        dis[begin] = 0
        next = [-1 for i in range(self.n)]
        queue = []
        queue.append(begin)
        while queue.__len__() > 0:
            for i in range(self.n):
                if self.adjacent[queue[0]][i] == 1 and dis[i] == -1:
                    dis[i] = dis[queue[0]] + 1
                    next[queue[0]] = i
                    if i == end:
                        j = begin
                        while j != end:
                            print(j, end = '->')
                            j = next[j]
                        print(j)
                        return dis[i]
                    queue.append(i)
            queue.remove(queue[0])


if __name__ == "__main__":
    graph1 = Graph()
    begin = int(input())
    end = int(input())
    dis = graph1.shortest_BFS(begin, end)
    print('distance = ', dis)
