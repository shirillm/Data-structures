timur, ruslan = input(), input()

rules = {"камень": "ножницы", "ножницы": "бумага", "бумага": "камень"}

print("ничья" if timur == ruslan else "Тимур" if rules[timur] == ruslan else "Руслан")
