# Задаем список
spicok = []
spicok_sort = []

# Добавляем список
perebor2 = int(input('Введите сколько чисел хотите добавить: '))
for perebor in range(0, perebor2):
    spicok.append(input('Введите числа для добавления в список: '))

# Перебераем список и переносим его в другой
for perebor1 in range(0, len(spicok)):
    if int(spicok[perebor1]) % 2 == 0:
        spicok_sort.append(spicok[perebor1])
    else:
        spicok_sort.append(0)

print(spicok_sort)
