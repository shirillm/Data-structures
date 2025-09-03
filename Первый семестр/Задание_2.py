# Импортируем библиотеку
from math import *

# Переменные
A1 = int(input("Введите A1: "))
B1 = int(input("Введите B1: "))
C1 = int(input("Введите C1: "))

A2 = int(input("Введите A2: "))
B2 = int(input("Введите B2: "))
C2 = int(input("Введите C2: "))

# Вычисляем определитель
D = (A1 * B2) - (A2 * B1)

# Вычисляем x и y
x = (C1 * B2 - C2 * B1) / D
y = (A1 * C2 - A2 * C1) / D

# Выводим результат
print("x =", x)
print("y =", y)
