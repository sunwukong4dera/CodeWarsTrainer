def is_prime(num):
    if num <= 1:
        return False
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            return False
    return True

print(is_prime(1))
print(is_prime(3))
print(is_prime(6))