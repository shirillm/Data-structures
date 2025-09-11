text = input()  # читаем строку
price_kop = len(text) * 60  # считаем стоимость в копейках

rub = price_kop // 100      # целые рубли
kop = price_kop % 100       # остаток копеек

print(f"{rub} р. {kop} коп.")
