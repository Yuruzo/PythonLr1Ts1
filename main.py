
import math

def count_even_not_coprime(n):
    count = 0
    for i in range(2, n + 1, 2):
        if math.gcd(n, i) != 1:
            count += 1
    return count

def max_digit_not_divisible_by_three(n):
    max_digit = -1
    for digit in str(n):
        digit_int = int(digit)
        if digit_int % 3 != 0 and digit_int > max_digit:
            max_digit = digit_int
    return max_digit

def product_max_not_coprime_and_sum_digits_less_than_five(n):
    def smallest_divisor(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i
        return n

    def sum_digits_less_than_five(n):
        return sum(int(digit) for digit in str(n) if int(digit) < 5)

    min_divisor = smallest_divisor(n)
    max_not_coprime = -1

    for i in range(2, n):
        if math.gcd(n, i) != 1 and i % min_divisor != 0:
            if i > max_not_coprime:
                max_not_coprime = i

    sum_digits = sum_digits_less_than_five(n)
    return max_not_coprime * sum_digits
