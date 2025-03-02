
def count_numbers_less_than_five(s):
    
    # Задание 6: Подсчет количества чисел в строке, значение которых меньше 5.
    # :param s: Входная строка.
    # :return: Количество чисел меньше 5.
  
    numbers = [int(word) for word in s.split() if word.isdigit()]  # Извлекаем числа из строки
    return sum(1 for num in numbers if num < 5)  # Считаем числа меньше 5

s = "1 2 3 4 5 6 7 8 9"
print("Количество чисел меньше 5:", count_numbers_less_than_five(s))  
