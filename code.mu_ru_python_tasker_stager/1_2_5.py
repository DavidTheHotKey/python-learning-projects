"""
Даны два числа. Проверьте, что первые цифры этих чисел совпадают.
"""
number_1 = input("Введите число 1\n")
number_2 = input("Введите число 2\n")
if not (number_1.isdigit() and number_2.isdigit() and len(number_1) != 0 and len(number_2) != 0):
    print("ошибка: вы ввели неправильное число, или не число вовсе, просьба перепроверить входные данные")
elif str(number_1)[0] == str(number_2)[0]:
    print("Первые цифры совпадают")
else:
    print("Первые цирфы не совпадают")
