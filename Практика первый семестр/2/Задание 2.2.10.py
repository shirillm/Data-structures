n = int(input().strip())
infected = []

for idx in range(n):
    s = input().strip()
    target = "anton"
    pos = 0
    for char in s:
        if pos < len(target) and char == target[pos]:
            pos += 1
        if pos == len(target):
            infected.append(str(idx + 1))

print(" ".join(infected))

