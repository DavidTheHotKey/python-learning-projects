"""
Дан список. Удалите из него элементы с заданным значением.
"""
def main():
    try:
        my_list = []

        # Ввод элемента для удаления
        element_to_delete = input("Введите элемент, который вы хотите удалить из списка: ")

        print("Добавляйте элементы в список (для завершения ввода нажмите Enter без ввода текста):")

        # Ввод элементов списка
        while True:
            element = input()
            if element == "":
                print("Завершаем формирование списка...")
                break
            my_list.append(element)

        # Вывод исходного списка
        print(f"\nИсходный список: {my_list}")

        # Удаление элемента с помощью list comprehension
        original_length = len(my_list)
        my_list = [item for item in my_list if item != element_to_delete]
        removed_count = original_length - len(my_list)

        # Вывод результата
        print(f"Удалено элементов: {removed_count}")
        print(f"Итоговый список: {my_list}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()