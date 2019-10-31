# -*- coding: utf-8 -*-



def sum_nums(low, high):
    if low > high:
        print("error")
        return
    sumnum = 0
    while low <= high:
        sumnum += low
        low += 1
    return sumnum



if __name__ == '__main__':
    print("Please input low and high numbers:")
    low = int(input())
    high = int(input())
    result = sum_nums(low, high)
    if result:
        print(result)
    
