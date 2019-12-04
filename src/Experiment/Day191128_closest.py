# -*- coding: utf-8 -*-

import math



def input_data():
    try:
        infile = open('closest.in', 'r')
        f = [int(i) for i in infile.read().split()]
        infile.close()
    except IOError:
        f = [int(i) for i in input().split()]

    return f



if __name__ == "__main__":
	input_data()
