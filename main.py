
def elements_between_first_and_last_max(arr):

    # ������� 17: ���������� ��������� ����� ������ � ��������� ������������.
    # :param arr: ������������� ������.
    # :return: ������ ���������.

    max_val = max(arr)
    first_idx = arr.index(max_val)
    last_idx = len(arr) - arr[::-1].index(max_val) - 1
    return arr[first_idx+1:last_idx]

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("�������� ����� ������ � ��������� ������������ :", elements_between_first_and_last_max(arr))
