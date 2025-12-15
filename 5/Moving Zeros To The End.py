def move_zeros(lst: list) -> list:
    return [el for el in lst if el] + [0] * lst.count(0)

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))