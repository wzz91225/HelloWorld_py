def fun(n, s: str):
    l = s.__len__()
    if l == n:
        result.append(s)
    elif l == 0:
        fun(n, "0")
        fun(n, "1")
    else:
        fun(n, s + "0")
        if s[l - 1] == '0':
            fun(n, s + "1")




if __name__ == "__main__":
    result = []
    fun(3, "")
    print(result)
