
def count_digits_greater_than_five(s):
    
    # ������� 8: ������� ���������� ���� � ������, �������� ������� ������ 5.
    # :param s: ������� ������.
    # :return: ���������� ���� ������ 5.
 
    return sum(1 for char in s if char.isdigit() and int(char) > 5)  # ������� ����� ������ 5

s = "123456789"
print("���������� ���� ������ 5:", count_digits_greater_than_five(s))
