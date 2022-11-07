print('Все возможные названия страны, после ввода введите 0')
s = input()
names = []
data = []

while s != '0':
    names.append(s)
    s = input()
print('вики')
data.append(input())
print('оф название')
data.append(input())
print('столица')
data.append(input())
print('основание')
data.append(input())
print('население')
data.append(input())
print('правление')
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
    print(f"'{names[i]}': ['{data[0]}', {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}, {data[7]}, {data[8]}, {data[9]}]")

