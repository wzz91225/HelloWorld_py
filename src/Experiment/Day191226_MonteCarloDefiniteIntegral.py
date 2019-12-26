# -*- coding: utf-8 -*-

import random
import math



def f(x):
    return x**2



def definite_integral(low: float, up: float, test_num: int):
    """MonteCarlo"""
    sum = 0
    for i in range(test_num):
        sum += f(random.uniform(low, up))
    
    return sum * (up - low) / test_num



if __name__ == "__main__":
    print(definite_integral(float(input()), float(input()), int(input())))
