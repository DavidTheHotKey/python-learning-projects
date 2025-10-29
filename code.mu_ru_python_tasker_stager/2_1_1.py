"""
Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.
Метод с готовыми строками
"""

strings = [
    "http://example.com",
    "https://google.com",
    "ftp://server.com",
    "HTTP://test.org",  # вариант с большими буквами
    "http://github.com",
    "just text",
    "www.site.com",
    "http://yandex.ru",
    "file://local",
    "random string",
    "http://stackoverflow.com"
]
result = [s for s in strings if s.startswith('https://')]
print(result)