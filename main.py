

def sort_by_consonant_vowel_difference(words):

    # ������� 11: ���������� ����� �� ������� ����� ����������� ��������� � �������.
    # :param words: ������ �����.
    # :return: ��������������� ������ �����.

    vowels = set('aeiou')
    def diff(word):
        consonant_count = sum(1 for char in word if char.lower() not in vowels)
        vowel_count = sum(1 for char in word if char.lower() in vowels)
        return abs(consonant_count - vowel_count)
    return sorted(words, key=diff)

words = ["hello", "world", "python", "programming", "algorithm"]
print("��������������� ������:", sort_by_consonant_vowel_difference(words))
