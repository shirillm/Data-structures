# Вводим переменные
Price = float(input('Введите цену за 1кг: '))
Count_st = 12

# Выполняем условие перебора
while Count_st <= 20:
    print(Price * Count_st / 10)
    Count_st += 2
