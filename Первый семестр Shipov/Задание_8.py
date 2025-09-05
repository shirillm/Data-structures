def swap_quarters(matrix):
	# Получаем количество строк и столбцов матрицы
	M = len(matrix)
	N = len(matrix[0])

	# Проверяем, что размерности матрицы четные
	if M % 2 != 0 or N % 2 != 0:
		raise ValueError("Размеры матрицы должны быть четными числами")

	# Вычисляем середины матрицы по строкам и столбцам
	mid_row = M // 2
	mid_col = N // 2

	# Проходим по всем элементам левой верхней и правой нижней четвертей
	for i in range(mid_row):
		for j in range(mid_col):
			# Сохраняем значение из левой верхней четверти
			temp = matrix[i][j]

			# Заменяем значение в левой верхней четверти на значение из правой нижней
			matrix[i][j] = matrix[i + mid_row][j + mid_col]

			# Заменяем значение в правой нижней четверти на сохраненное значение
			matrix[i + mid_row][j + mid_col] = temp

	return matrix

# Пример использования
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]
]

print("Исходная матрица:")
for row in matrix:
	print(row)

result = swap_quarters(matrix)

print("\nМатрица после обмена четвертей:")
for row in result:
	print(row)