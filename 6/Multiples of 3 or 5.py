def solution(number):
    lst = [i for i in range(1, number) if not(i % 3) or not(i % 5)]
    return sum(lst) if sum(lst) > 0 else 0

