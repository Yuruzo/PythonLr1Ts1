
def print_array_indices(arr):

    # Задание 15: Вывод индексов массива в порядке, соответствующем значениям.
    # :param arr: Целочисленный массив.
    # :return: Список индексов.

    return sorted(range(len(arr)), key=lambda i: arr[i])

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Индексы массива:", print_array_indices(arr))
