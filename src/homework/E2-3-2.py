def sum_nums_while(low, high):
    if low > high:
        print("error")
        return
    sumnum = 0
    while low <= high:
        sumnum += low
        low += 1
    return sumnum



def sum_nums_for(low, high):
    if low > high:
        print("error")
        return
    sumnum = 0
    for i in range(low, high + 1):
        sumnum += i
    return sumnum


if __name__ == "__main__":
    print(sum_nums_while(1, 100))
    print(sum_nums_for(1, 100))
    