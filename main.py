
def prime_factors(n):

    # ������� 19: ���������� ������ ���� ������� ��������� �����.
    # :param n: ����������� �����.
    # :return: ������ ������� ���������.

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

print("������� �������� ����� 28:", prime_factors(28))
