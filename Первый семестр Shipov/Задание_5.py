# Импортируем библиотеку
import math
from math import *

# Вводим переменные
n = int(input('Введите число n: '))

if n <= 0:
	print('1')
else:
	chislo = 1
	for perebor in range(0, n + 1):
		chislo += 1 / math.factorial(perebor)
print(chislo)
