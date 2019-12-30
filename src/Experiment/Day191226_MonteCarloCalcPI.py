# -*- coding: utf-8 -*-

import random
import math



def calc_pi(test_num: int):
    """MonteCarlo"""
    in_num = 0
    for i in range(test_num):
        x = random.random()
        y = random.random()
        if math.sqrt(x**2 + y**2) < 1:
            in_num += 1
    return in_num / test_num * 4



if __name__ == "__main__": 
    print('Please Input Test Num:', end = '\n  ')
    test_num = int(input())
    print('Pi = ', calc_pi(test_num))
