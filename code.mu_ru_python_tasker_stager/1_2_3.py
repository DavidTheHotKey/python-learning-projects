"""
Дано число. Выведите в консоль сумму первой и последней цифры этого числа.
С обработкой исключений и циклами
"""
try:
    number = input("Введите число: ")
    if not number.isdigit() or len(number) == 0:
        print("Ошибка: введите корректное число")
    else:
        result = int(number[0]) + int(number[-1])
        print(f"Сумма первой и последней цифры: {result}")
except ValueError:
    print("Ошибка: введите числовое значение")