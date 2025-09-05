# а) Вывод уникальных цифр числа в возрастающем порядке
def unique_digits_ascending(number):
    # Преобразуем число в строку, чтобы работать с каждой цифрой
    num_str = str(number)

    # Создаем множество из цифр (автоматически удаляет дубликаты)
    unique_digits = set(num_str)

    # Фильтруем только цифры (игнорируем знак минус для отрицательных чисел)
    digits_only = {d for d in unique_digits if d.isdigit()}

    # Сортируем цифры в возрастающем порядке и выводим
    sorted_digits = sorted(digits_only)
    print("Уникальные цифры в возрастающем порядке:", sorted_digits)

    return sorted_digits


# б) Проверка, является ли A строгим подмножеством B
def is_strict_subset(A, B):
    # Проверяем, что все элементы A есть в B, и что B имеет дополнительные элементы
    is_subset = A.issubset(B)
    has_additional = len(B) > len(A)

    # Выводим результат проверки
    if is_subset and has_additional:
        print("Множество A является строгим подмножеством множества B")
        return True
    else:
        print("Множество A НЕ является строгим подмножеством множества B")
        return False


# Демонстрация работы функций
if __name__ == "__main__":
    print("Часть а):")
    number = int(input("Введите число: "))
    unique_digits_ascending(number)

    print("\nЧасть б):")
    # Примеры множеств
    A = {1, 2, 3}
    B = {1, 2, 3, 4, 5}
    C = {1, 2, 3}
    D = {1, 2, 4}

    print("Множество A:", A)
    print("Множество B:", B)
    is_strict_subset(A, B)

    print("\nМножество A:", A)
    print("Множество C:", C)
    is_strict_subset(A, C)

    print("\nМножество A:", A)
    print("Множество D:", D)
    is_strict_subset(A, D)
