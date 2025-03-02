
def sort_by_vowel_consonant_pairs(words):

    # Задание 13: Сортировка строк по разнице между количеством сочетаний «гласная-согласная» и «согласная-гласная».
    # :param words: Список строк.
    # :return: Отсортированный список строк.

    vowels = set('aeiou')
    def pair_diff(word):
        vc = 0
        cv = 0
        for i in range(len(word) - 1):
            if word[i].lower() in vowels and word[i+1].lower() not in vowels:
                vc += 1
            elif word[i].lower() not in vowels and word[i+1].lower() in vowels:
                cv += 1
        return abs(vc - cv)
    return sorted(words, key=pair_diff)

words = ["hello", "world", "python", "programming", "algorithm"]
print("Отсортированные строки:", sort_by_vowel_consonant_pairs(words))
