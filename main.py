
def sort_by_ascii_triple_deviation(words):

    # Задание 14: Сортировка строк по квадратичному отклонению дисперсии максимального среднего веса ASCII-кода тройки символов.
    # :param words: Список строк.
    # :return: Отсортированный список строк.

    def ascii_triple_avg(word):
        max_avg = 0
        for i in range(len(word) - 2):
            avg = (ord(word[i]) + ord(word[i+1]) + ord(word[i+2])) / 3
            if avg > max_avg:
                max_avg = avg
        return max_avg
    first_max_avg = ascii_triple_avg(words[0])
    def deviation(word):
        return (ascii_triple_avg(word) - first_max_avg) ** 2
    return sorted(words, key=deviation)

words = ["hello", "world", "python", "programming", "algorithm"]
print("Отсортированные строки:", sort_by_ascii_triple_deviation(words))
