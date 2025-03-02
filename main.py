

def sort_by_consonant_vowel_difference(words):

    # Задание 11: Сортировка строк по разнице между количеством согласных и гласных.
    # :param words: Список строк.
    # :return: Отсортированный список строк.

    vowels = set('aeiou')
    def diff(word):
        consonant_count = sum(1 for char in word if char.lower() not in vowels)
        vowel_count = sum(1 for char in word if char.lower() in vowels)
        return abs(consonant_count - vowel_count)
    return sorted(words, key=diff)

words = ["hello", "world", "python", "programming", "algorithm"]
print("Отсортированные строки:", sort_by_consonant_vowel_difference(words))
