def next_bigger(n):
    digits = list(str(n))

    # находим индекс первой цифры, которую можно увеличить
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1

    # находим наименьшую цифру справа, которая больше digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # меняем местами
    digits[i], digits[j] = digits[j], digits[i]

    # сортируем хвост по возрастанию (можно реверснуть, так как он уже в убывающем порядке)
    digits[i + 1:] = reversed(digits[i + 1:])

    result = int(''.join(digits))

    # проверяем, что не добавились ведущие нули
    return result if result > n else -1


print(next_bigger(1289))
