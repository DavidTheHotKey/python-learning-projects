"""Выведите в консоль все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти."""
def sum_of_first_and_second_digits(x):
    digits = str(x)
    return int(digits[0]) + int(digits[1])
try:
    list_of_numbers_needed = []
    for x in range(10, 1001):
        if sum_of_first_and_second_digits(x) == 5:
            list_of_numbers_needed.append(str(x))
    print(f"Искомый список, в котором все числа в промежутке от 10 до 1000, сумма первой и второй цифры которых равна пяти:\n{', '.join(list_of_numbers_needed)}")
except Exception as e:
    print(f"Произошла ошибка: {e}")