
def count_words(s):
    
    # Задание 3: Подсчет количества слов в строке.
    # :param s: Входная строка.
    # :return: Количество слов.
    
    return len(s.split())  # Разделяем строку по пробелам и считаем количество элементов
    
    s = "Hello world, this is a test"
print("Количество слов в строке:", count_words(s))  

