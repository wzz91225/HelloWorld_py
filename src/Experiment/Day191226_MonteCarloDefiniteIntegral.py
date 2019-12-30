# -*- coding: utf-8 -*-

import random
import math



def f(x):
    return x**2 + math.sin(x) + 2 * x - 6



def definite_integral(low: float, up: float, test_num: int):
    """MonteCarlo"""
    sum = 0
    for i in range(test_num):
        sum += f(random.uniform(low, up))
    
    return sum * (up - low) / test_num



if __name__ == "__main__":
    print('Please Input Low Num:', end = '\n  ')
    low = float(input())
    print('Please Input Up Num:', end = '\n  ')
    up = float(input())
    print('Please Input Test Num:', end = '\n  ')
    test_num = int(input())
    print('Result:', end = '\n  ')
    print(definite_integral(low, up, test_num))
