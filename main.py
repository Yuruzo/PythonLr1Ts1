
def sort_by_most_frequent_char(words):

    # Задание 12: Сортировка строк по квадратичной встречаемости самого частого символа.
    # :param words: Список строк.
    # :return: Отсортированный список строк.

    from collections import Counter
    def most_freq_char(word):
        counter = Counter(word)
        most_common = counter.most_common(1)[0][1]
        return most_common ** 2
    return sorted(words, key=most_freq_char)

words = ["hello", "world", "python", "programming", "algorithm"]
print("Отсортированные строки:", ort_by_most_frequent_char(words))
