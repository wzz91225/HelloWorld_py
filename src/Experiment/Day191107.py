# -*- coding: utf-8 -*-


def RecursionFun(i: int):
    result = 1 / i
    if i > 1:
        result += RecursionFun(i - 1)
    print(result)
    return result 


if __name__ == "__main__":
    RecursionFun(13)
