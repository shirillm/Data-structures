s = input() + " запретил букву"
alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

for c in alphabet:
    if c in s:
        print(s, c)
        s = s.replace(c, "").replace("  ", " ").strip()
        