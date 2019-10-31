def fun(n, m, s: str):
    if n == 0:
        print(s)
        return
    if s.__len__() != 0:
        s += "+"
    for i in range(m, 0, -1):
        n1 = n - i
        m1 = i
        if i > n1:
            m1 = n1
        fun(n1, m1, s + str(i))



if __name__ == "__main__":
    fun(6, 6, "")
