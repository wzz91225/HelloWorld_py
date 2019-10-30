def get_prime_factor(n):
    result = [1, ]

    while n % 2 == 0:
        result.append(2)
        n //= 2

    for i in range(3, n // 2 + 1, 2):
        while n % i == 0:
            result.append(i)
            n //= i

    if n != 1:
        result.append(n)

    return result


def perfect_num(n):
    print(1)
    for i in range(2, n + 1):
        if sum(get_prime_factor(i)) == i:
            print(i)



if __name__ == "__main__":
    perfect_num(1000)
