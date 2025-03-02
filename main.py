
def sort_by_length():

    # Задание 9: Упорядочивание строк по длине.
    # :return: Отсортированный список строк.

    # Чтение строк с клавиатуры
    lines = []
    print("Введите строки (для завершения введите пустую строку):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    # Сортировка строк по длине
    sorted_lines = sorted(lines, key=len)
    return sorted_lines

# Пример использования
print("Отсортированные строки по длине:", sort_by_length())
