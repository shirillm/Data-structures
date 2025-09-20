num = input().strip()

# Если число 6-значное, отделяем первую цифру
if len(num) == 6:
    first = num[0]
    last_five = num[1:]
    reversed_five = last_five[::-1]
    result = first + str(int(reversed_five))  # int убирает ведущие нули
else:
    last_five = num
    reversed_five = last_five[::-1]
    result = str(int(reversed_five))

print(result)
