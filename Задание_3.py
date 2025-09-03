# Импортируем библиотеку
from math import *

# Вводим переменные
x = float(input("Введите x: "))
a = float(input("Введите a: "))

# Вычисляем по условию
if x > 1:
    y = 2 * a * (x ** 2) - 1
else:
    y = 1 / a

# Вывод
print("y =", y)
