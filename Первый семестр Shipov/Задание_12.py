# а) Проверяет, содержит ли кортеж элемент и выводит количество вхождений
def check_tuple_element(tuple_data, element):
    # Проверяем наличие элемента в кортеже
    if element in tuple_data:
        # Считаем количество вхождений элемента
        count = tuple_data.count(element)
        print(f"Элемент '{element}' найден в кортеже. Количество вхождений: {count}")
        return count
    else:
        print(f"Элемент '{element}' не найден в кортеже.")
        return 0


# б) Преобразует список строк в кортеж без повторяющихся элементов
def list_to_unique_tuple(string_list):
    # Преобразуем список в множество для удаления дубликатов, затем в кортеж
    unique_tuple = tuple(set(string_list))
    print(f"Кортеж без повторений: {unique_tuple}")
    return unique_tuple


# Демонстрация работы функций
if __name__ == "__main__":
    # Пример для части а)
    print("Часть а):")
    my_tuple = ('apple', 'banana', 'orange', 'apple', 'grape')
    user_element = input("Введите элемент для поиска в кортеже: ")
    check_tuple_element(my_tuple, user_element)

    # Пример для части б)
    print("\nЧасть б):")
    user_input = input("Введите строки через запятую: ")
    string_list = [s.strip() for s in user_input.split(',')]
    list_to_unique_tuple(string_list)
