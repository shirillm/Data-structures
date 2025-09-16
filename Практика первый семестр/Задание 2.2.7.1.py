timur = input().strip()
ruslan = input().strip()

if timur == ruslan:
    print("ничья")
elif (timur == "камень" and ruslan == "ножницы") or \
(timur == "ножницы" and ruslan == "бумага") or \
(timur == "бумага" and ruslan == "камень"):
    print("Тимур")
else:
    print("Руслан")
    