# -*- coding: utf-8 -*-

# from MergeSort import MergeSort



def delete_problem(f, index, k):
    pass



if __name__ == "__main__":
    print("Please Input Target Number:", end = "\n  ")
    f = list(map(lambda x: int(x), input().strip()))
    print("Please Input k ∈ [0, ", f.__len__(), "):", sep = "", end = "\n  ")
    k = int(input())
    delete_problem(f, 0, k)
