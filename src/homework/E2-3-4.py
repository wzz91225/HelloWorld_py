def merge_dict(d1:dict, d2:dict):
    for key, value in d2.items():
        if d1.__contains__(key):
            d1[key] += value
        else:
            d1.update(key = value)
    return d1



if __name__ == "__main__":
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    result = merge_dict(d1, d2)
    print(result)
    