def sum_nums(low, high):
    if low > high:
        print("error")
        return
    sumnum = 0
    while low <= high:
        sumnum += low
        low += 1
    return sumnum



if __name__ == "__main__":
    result = sum_nums(2,10)
    if result:
        print(result)
