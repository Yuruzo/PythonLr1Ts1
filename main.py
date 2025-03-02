
def sort_by_word_count():

    # Задание 10: Упорядочивание строк по количеству слов.
    # :return: Отсортированный список строк.

    # Чтение строк с клавиатуры
    lines = []
    print("Введите строки (для завершения введите пустую строку):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    # Сортировка строк по количеству слов
    sorted_lines = sorted(lines, key=lambda x: len(x.split()))
    return sorted_lines

# Пример использования
print("Отсортированные строки по количеству слов:", sort_by_word_count())

