
def print_array_indices(arr):

    # ������� 15: ����� �������� ������� � �������, ��������������� ���������.
    # :param arr: ������������� ������.
    # :return: ������ ��������.

    return sorted(range(len(arr)), key=lambda i: arr[i])

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("������� �������:", print_array_indices(arr))
