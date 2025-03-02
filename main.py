
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
