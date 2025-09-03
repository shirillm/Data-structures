import pandas as pd


def swap_quarters(matrix):
	m = len(matrix)
	n = len(matrix[0])
	half_m = m // 2
	half_n = n // 2
	for i in range(half_m):
		for j in range(half_n):
			matrix[i][j], matrix[i + half_m][j + half_n] = matrix[i + half_m][j + half_n], matrix[i][j]
	return matrix


# Пути к файлам
input_file = "matrix.xlsx"
output_file = "matrix_new.xlsx"

# Читаем матрицу из Excel
df = pd.read_excel(input_file, header=None)
matrix = df.values.tolist()

# Меняем четверти
matrix_new = swap_quarters(matrix)

# Сохраняем результат в новый Excel
pd.DataFrame(matrix_new).to_excel(output_file, index=False, header=False)

print(f"Матрица успешно обработана! Результат сохранён в {output_file}")
