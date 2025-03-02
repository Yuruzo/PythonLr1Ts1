
def count_numbers_less_than_five(s):
    
    # ������� 6: ������� ���������� ����� � ������, �������� ������� ������ 5.
    # :param s: ������� ������.
    # :return: ���������� ����� ������ 5.
  
    numbers = [int(word) for word in s.split() if word.isdigit()]  # ��������� ����� �� ������
    return sum(1 for num in numbers if num < 5)  # ������� ����� ������ 5

s = "1 2 3 4 5 6 7 8 9"
print("���������� ����� ������ 5:", count_numbers_less_than_five(s))  
