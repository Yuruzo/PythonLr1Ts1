
def sort_by_most_frequent_char(words):

    # ������� 12: ���������� ����� �� ������������ ������������� ������ ������� �������.
    # :param words: ������ �����.
    # :return: ��������������� ������ �����.

    from collections import Counter
    def most_freq_char(word):
        counter = Counter(word)
        most_common = counter.most_common(1)[0][1]
        return most_common ** 2
    return sorted(words, key=most_freq_char)

words = ["hello", "world", "python", "programming", "algorithm"]
print("��������������� ������:", ort_by_most_frequent_char(words))
