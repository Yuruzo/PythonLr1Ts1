
def elements_between_first_and_second_max(arr):

    # Задание 16: Нахождение элементов между первым и вторым максимальным.
    # :param arr: Целочисленный массив.
    # :return: Список элементов.

    max1 = max(arr)
    idx1 = arr.index(max1)
    max2 = max([x for i, x in enumerate(arr) if i != idx1])
    idx2 = arr.index(max2)
    return arr[min(idx1, idx2)+1:max(idx1, idx2)]

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Элементы между первым и вторым максимальным:", elements_between_first_and_second_max(arr))
