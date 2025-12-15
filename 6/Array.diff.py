def array_diff(a: list, b: list) -> list:
    for index in range(len(b)):
        while b[index] in a:
            a.remove(b[index])
    return a


print(array_diff([1, 2, 2], [2]))