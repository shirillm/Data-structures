# Импортируем библиотеки
import math
from math import *

# x**2 - в квадрате
# math.cos(X) - косинус X (X указывается в радианах)

# Переменные
y = x = a = None

# Задаем переменные
y = int(input())
x = int(input())
a = int(input())

# Составляем выражение на вывод

y = (a / (x ** 2 + 1)) - math.cos(2 * x - 1)

# Принтим
print(y)
