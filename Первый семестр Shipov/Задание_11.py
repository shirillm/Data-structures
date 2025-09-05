# Вычисляем сумму всех значений в словаре
def sum_dict_values(dictionary):
    return sum(dictionary.values())


# Преобразуем список в словарь с пустыми значениями
def list_to_nested_dict(lst):
    return {item: {} for item in lst}


# Проверяем, все ли значения в словаре одинаковые
def all_values_equal(dictionary):
    return len(set(dictionary.values())) == 1


# Демонстрация работы
test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(sum_dict_values(test_dict))  # 10

test_list = ['a', 'b', 'c']
print(list_to_nested_dict(test_list))  # {'a': {}, 'b': {}, 'c': {}}

test_dict_equal = {'a': 1, 'b': 1, 'c': 1}
print(all_values_equal(test_dict_equal))  # True
