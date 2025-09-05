def reverse_if_multiple_of_four(s):
    # Получаем длину строки
    length = len(s)

    # Проверяем, делится ли длина на 4 без остатка
    if length % 4 == 0:
        # Создаем пустую строку для результата
        reversed_string = ""

        # Проходим по строке в обратном порядке
        for i in range(length - 1, -1, -1):
            # Добавляем символы в новую строку
            reversed_string += s[i]

        return reversed_string
    else:
        # Возвращаем исходную строку без изменений
        return s
