
import math

def count_even_not_coprime(n):
    count = 0
    for i in range(2, n + 1, 2):
        if math.gcd(n, i) != 1:
            count += 1
    return count
