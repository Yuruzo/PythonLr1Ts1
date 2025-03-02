

def find_unused_latin_chars(s):

    # Задание 7: Поиск незадействованных символов латиницы в строке.
    # :param s: Входная строка.
    # :return: Множество незадействованных символов латиницы.

    used_chars = set(s.lower())  # Собираем использованные символы
    latin_chars = set('abcdefghijklmnopqrstuvwxyz')  # Все символы латиницы
    return latin_chars - used_chars  # Разница между всеми символами и использованными

s = "Hello world"
print("Незадействованные символы латиницы:", find_unused_latin_chars(s))
