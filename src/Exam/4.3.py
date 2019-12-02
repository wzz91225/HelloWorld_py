# -*- coding: utf-8 -*-



def factorial_recursion(n :int):
    if n < 0:
        return "error"
    elif n <= 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)



if  __name__ == "__main__":
    print(factorial_recursion(int(input())))
