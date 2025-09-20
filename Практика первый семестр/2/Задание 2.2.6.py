n = int(input())
numbers = [int(input()) for _ in range(n)]
x = int(input())

found = False

for i in range(n):
    for j in range(n):
        if i != j and numbers[i] * numbers[j] == x:
            found = True
            break
    if found:
        break

print("ДА" if found else "НЕТ")
