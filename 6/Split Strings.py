def solution(s: str):
    return [s[i * 2] + s[i * 2 + 1] for i in range(len(s) // 2)] + [(s[-1] + '_')] if (len(s) % 2) else \
        [s[i * 2] + s[i * 2 + 1] for i in range(len(s) // 2)]


print(solution('abcdefk1'))



