"""
Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.
Метод со строками, которые вводит пользователь
"""
def filter_http_urls(string_list):
    """Фильтрует строки, начинающиеся с http://"""
    return [s for s in string_list if s.startswith('http://')]

# Использование
try:
    import keyboard
    string_list=[]
    print("Напишите несколько строк текста, программа автоматически отфильтрует те строки-ссылки, где используется протокол HTTP! Для выхода нажмите ESC")
    while True:
        user_input = input()  # Сохраняем ввод пользователя
        string_list.append(user_input)  # Добавляем в список
        urls = filter_http_urls(string_list)
        print("Текущий список всех строк:", string_list)
        print("Отфильтрованные HTTP ссылки:", urls)
        print("---")
        if keyboard.is_pressed('esc'):
            print("Выход по нажатию ESC")
            break

except Exception as e:
    print(f"Произошла ошибка: {e}")