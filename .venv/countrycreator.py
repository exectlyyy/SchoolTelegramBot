print('Все возможные названия страны, после ввода введите 0')
s = input()
names = []
data = []

while s != '0':
    names.append(s)
    s = input()
    print('Ссылка на картинку флага')
    data.append(input())
    print('Название с википедии (полное)')
    data.append(input())
    print('Столица')
    data.append(input())
    print('Дата основания или независимости (указать)')
    data.append(input())
    print('численность населения в формате - 147 млн. человек')
    data.append(input())
    print('форма правления')
    data.append(input())
    print('правитель')
    data.append(input())
    print('язык')
    data.append(input())
    print('валюта')
    data.append(input())
    print('доп инфа')
    data.append(input())
for i in range(len(names)):
    print(f"'{names[i]}': ['{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', '{data[6]}', '{data[7]}', '{data[8]}', '{data[9]}']")

