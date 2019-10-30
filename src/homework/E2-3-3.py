def delete_duplication(f):
    i = 0
    while i < len(f) - 1:
        j = i + 1
        while j < len(f):
            if (f[i] == f[j]):
                f.pop(j)
            else:
                j += 1
        i += 1



if __name__ == "__main__":
    f = [1,2,3,4,5,6,4,3,2,1]
    delete_duplication(f)
    for a in f:
        print(a)
    