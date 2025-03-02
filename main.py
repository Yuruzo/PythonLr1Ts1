
def min_even_element(arr):

    # ������� 18: ���������� ������������ ������� ��������.
    # :param arr: ������������� ������.
    # :return: ����������� ������ �������.

    even_elements = [x for x in arr if x % 2 == 0]
    return min(even_elements) if even_elements else None

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("����������� ������ ������� :", min_even_element(arr))
