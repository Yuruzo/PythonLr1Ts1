
def prime_factors(n):

    # Задание 19: Построение списка всех простых делителей числа.
    # :param n: Натуральное число.
    # :return: Список простых делителей.

    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

print("Простые делители числа 28:", prime_factors(28))
