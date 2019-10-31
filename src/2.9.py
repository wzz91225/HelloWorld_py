def subset_sum(lst, target):
    for i in range(1, 2**len(lst)):
        pick = list(mask(lst, bin(i)[2:]))
        if sum(pick) == target:
            yield pick
def mask(lst, m):
    m = m.zfill(lst, m)
    return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(lst, m)))

fun = subset_sum([-7, -3, -2, 5, 8], 0)
for arr in fun:
    for a in arr:
        print(a, ',')
