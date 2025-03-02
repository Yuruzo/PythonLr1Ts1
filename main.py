
def count_digits_greater_than_five(s):
    
    # Задание 8: Подсчет количества цифр в строке, значение которых больше 5.
    # :param s: Входная строка.
    # :return: Количество цифр больше 5.
 
    return sum(1 for char in s if char.isdigit() and int(char) > 5)  # Считаем цифры больше 5

s = "123456789"
print("Количество цифр больше 5:", count_digits_greater_than_five(s))
