from threading import local
import telebot

from telebot import types
from random import *
from math import sqrt

bot = telebot.TeleBot('5670990101:AAHCY6UcN3pZC43P5FbVulljTAZVrlo4TWA');
user_data = {}			
country_data = {'Россия': ['https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/320px-Flag_of_Russia.svg.png', 'Российская Федерация', 'Москва', '25.12.1991', '147 млн. человек', 'республика', 'Владимир Владимирович Путин, президент РФ (на 2022)', 'русский', 'российский рубль, ₽ (RUB)'], 
				'Япония': ['https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/320px-Flag_of_Japan.svg.png', 'Япония', 'Токио', '11.02.660 до н.э.', '125 млн. человек', 'конституционная монархия', 'Нарухито, император\n Фумио Кисида, премьер-министр (на 2022)', 'японский', 'японская иена, ¥ (JPY)']}

@bot.message_handler(commands=['start'])			
def greetings(message):			#ФУНКЦИЯ СТАРТ	
	markup = types.ReplyKeyboardMarkup()    
	HelpMarkup = types.KeyboardButton('/help')  
	markup.add(HelpMarkup)
	bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}, этот бот поможет тебе в решении задач по таким предметам как физика.', reply_markup=markup)

@bot.message_handler(commands=['cat'])				
def cat(message):				#ФУНКЦИЯ С КОТАМИ
	list_cats = ['https://ferma-biz.ru/wp-content/uploads/2022/08/QPdAc.jpg', 'https://ferma-biz.ru/wp-content/uploads/2022/08/koty-50.jpg', 'https://fydi.ru/wp-content/uploads/2021/08/koty-i-koshki-93.jpg']
	bot.send_photo(message.from_user.id, photo = choice(list_cats))

@bot.message_handler(commands=['help'])
def help(message):				#ФУНКЦИЯ ПОМОЩИ
	global user_data
	user_data[message.from_user.id] = []
	markup = types.ReplyKeyboardMarkup() 
	clear_markup1 = types.KeyboardButton('Решение задач') 
	clear_markup2 = types.KeyboardButton('Справочные материалы') 
	clear_markup3 = types.KeyboardButton('Конвертер величин') 
	markup.add(clear_markup1, clear_markup2, clear_markup3)
	bot.send_message(message.from_user.id, f'Список команд:\n  /clear -  очищает актуальный кэш бота и возвращает к началу.\n /cat -  отправляет фотографию котика, чтобы скрасить тяжелые будни)\n\n   {message.from_user.first_name}, напиши "решение задач" или "справочные материалы"', reply_markup=markup)

@bot.message_handler(commands=['clear'])
def clear(message):				#ФУНКЦИЯ ОЧИСТКИ
	global user_data
	user_data[message.from_user.id] = []
	markup = types.ReplyKeyboardMarkup() 
	clear_markup1 = types.KeyboardButton('Решение задач') 
	clear_markup2 = types.KeyboardButton('Справочные материалы') 
	clear_markup3 = types.KeyboardButton('Конвертер величин') 
	markup.add(clear_markup1, clear_markup2, clear_markup3)
	bot.send_message(message.from_user.id, 'История очищена!', reply_markup=markup)

@bot.message_handler(content_types=['text'])			
def main(message):
	global user_data			
	global country_data																									#СОЗДАЕТ ПЕРЕМЕННУЮ, ЗАПОМИНАЮЩУЮ СООБЩЕНИЯ
	if message.from_user.id not in user_data: 																			#СОЗДАЕТ ПЕРЕМЕННУЮ, ЗАПОМИНАЮЩУЮ СООБЩЕНИЯ
		user_data[message.from_user.id] = []
	local_data = user_data[message.from_user.id]
	if len(local_data) == 0:																							#ОСНОВНАЯ ВЕТКА (РЕШЕНИЕ ЗАДАЧ\СПРАВОЧНЫЕ МАТЕРИАЛЫ)
		if message.text.lower() == 'решение задач':
			markup = types.ReplyKeyboardMarkup()    
			SubjectButton1 = types.KeyboardButton('Физика') 
			SubjectButton2 = types.KeyboardButton('Математика') 
			markup.add(SubjectButton1, SubjectButton2)
			bot.send_message(message.from_user.id, "Выберите предмет", reply_markup=markup)
			local_data.append(message.text.lower())
		elif message.text.lower() == 'справочные материалы':
			markup = types.ReplyKeyboardMarkup()    
			SubjectButton1 = types.KeyboardButton('География')
			markup.add(SubjectButton1)
			bot.send_message(message.from_user.id, "Выберите предмет", reply_markup=markup)
			local_data.append(message.text.lower())
		elif message.text.lower() == 'конвертер величин':
			markup = types.ReplyKeyboardMarkup()    
			TypeButton1 = types.KeyboardButton('Скорость')
			markup.add(TypeButton1)
			bot.send_message(message.from_user.id, "Выберите тип величины", reply_markup=markup)
			local_data.append(message.text.lower())
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, для помощи напиши команду  /help')
	elif len(local_data) == 1 and local_data[0] == 'справочные материалы': 													#ВЕТКА СПРАВОЧНЫЕ МАТЕРИАЛЫ
		local_data.append(message.text.lower())
		markup = types.ReplyKeyboardRemove(selective=False)
		if local_data[1] == 'география':
			bot.send_message(message.from_user.id, 'Введи название страны, что бы получить основную информацию о ней:', reply_markup=markup)
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, для помощи напиши команду  /help', reply_markup=markup)
	elif len(local_data) == 1 and local_data[0] == 'конвертер величин': 													#ВЕТКА СПРАВОЧНЫЕ МАТЕРИАЛЫ
		local_data.append(message.text.lower())
		markup = types.ReplyKeyboardRemove(selective=False)
		if local_data[1] == 'скорость':
			bot.send_message(message.from_user.id, 'Введи числовое значение величины', reply_markup=markup)
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, для помощи напиши команду  /help', reply_markup=markup)
	elif len(local_data) == 2 and local_data[0] == 'справочные материалы' and local_data[1] == 'география':						#ВЫВОДИТ СПРАВКУ О СТРАНАХ			markup = types.ReplyKeyboardRemove(selective=False)
		markup = types.ReplyKeyboardRemove(selective=False)
		if message.text.title() in country_data:
			local_data.append(message.text.lower())
			text = f''' ▻{country_data[str(local_data[2].title())][1]}◅ 
					  ●Столица: {country_data[str(local_data[2].title())][2]}
					  ●Дата основания: {country_data[str(local_data[2].title())][3]}
					  ●Численность населения: {country_data[str(local_data[2].title())][4]}
					  ●Форма правления: {country_data[str(local_data[2].title())][5]}
					  ●Глава государства и должность: {country_data[str(local_data[2].title())][6]}
					  ●Официльный(е) язык(и): {country_data[str(local_data[2].title())][7]}
					  ●Валюта: {country_data[str(local_data[2].title())][8]}\n'''
			bot.send_photo(message.from_user.id, photo=country_data[local_data[2].title()][0], caption=text)
			user_data[message.from_user.id] = []    
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, видимо в нашей базе ещё нет этой страны.', reply_markup=markup)
	elif len(local_data) == 1 and local_data[0] == 'решение задач':														#ВЕТКА РЕШЕНИЕ ЗАДАЧ
		if message.text.lower() == 'физика':
			markup = types.ReplyKeyboardMarkup()
			physchapter1 = types.KeyboardButton('Термодинамика')
			markup.add(physchapter1)
			bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
			local_data.append(message.text.lower())
		elif message.text.lower() == 'математика':
			markup = types.ReplyKeyboardMarkup()
			physchapter1 = types.KeyboardButton('Алгебра')
			markup.add(physchapter1)
			bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
			local_data.append(message.text.lower())
		else:
			markup = types.ReplyKeyboardMarkup()    
			SubjectButton1 = types.KeyboardButton('Физика') 
			SubjectButton2 = types.KeyboardButton('Математика') 
			markup.add(SubjectButton1, SubjectButton2)
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, выбери нужный тебе предмет:', reply_markup=markup)
	elif len(local_data) == 2 and message.text.lower() == 'термодинамика' or message.text.lower() == 'алгебра':																								#ВЕТКА С КОНКРЕТНЫМИ ЗАДАЧАМИ
		if message.text.lower() == 'термодинамика':
			markup = types.ReplyKeyboardMarkup()
			PhysicsThermodynamics1 = types.KeyboardButton('Q')
			PhysicsThermodynamics2 = types.KeyboardButton('c')
			PhysicsThermodynamics3 = types.KeyboardButton('t₁')
			PhysicsThermodynamics4 = types.KeyboardButton('t₂')
			PhysicsThermodynamics5 = types.KeyboardButton('m')
			markup.add(PhysicsThermodynamics1, PhysicsThermodynamics2, PhysicsThermodynamics3, PhysicsThermodynamics4, PhysicsThermodynamics5)
			bot.send_message(message.from_user.id, "Выберите неизвестное", reply_markup=markup)
			local_data.append(message.text.lower())
		elif message.text.lower() == 'алгебра':
			markup = types.ReplyKeyboardMarkup()
			math1 = types.KeyboardButton('Квадратные уравнения')
			markup.add(math1)
			bot.send_message(message.from_user.id, "Выберите тип задачи:", reply_markup=markup)
			local_data.append(message.text.lower())
		else:
			markup = types.ReplyKeyboardRemove(selective=False)
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, выбери нужный тебе раздел:', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'квадратные уравнения':												#ВВОД КОЭФ УРАВНЕНИЯ
		bot.send_message(message.from_user.id, "Введите коэффиценты уравнения через пробел.")
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 'квадратные уравнения':												#ВЕТКА РЕШЕНИЯ УРАВНЕНИЯ ДОПИЛИТЬ!!!
		cf = message.text.split()
		if len(cf) == 3 and float(cf[0]) != 0:
			cf[0] = float(cf[0])
			cf[1] = float(cf[1])
			cf[2] = float(cf[2])
			bot.send_message(message.from_user.id, f'''---Уравнение---
{cf[0]}x²+{cf[1]}x+{cf[2]}=0
D = {cf[1]}² - 4 * {cf[0]} * {cf[2]} = {(cf[1] ** 2) - 4 * cf[0] * cf[2]}
x₁ = -{cf[1]} + √D / 2 * {cf[0]} = {(cf[1] + sqrt((cf[1] ** 2) - 4 * cf[0] * cf[2])) / 2 * cf[0]}
x₂ = -{cf[1]} - √D / 2 * {cf[0]} = {(cf[1] - sqrt((cf[1] ** 2) - 4 * cf[0] * cf[2])) / 2 * cf[0]}
Ответ: {(cf[1] + sqrt((cf[1] ** 2) - 4 * cf[0] * cf[2])) / 2 * cf[0]}, {(cf[1] - sqrt((cf[1] ** 2) - 4 * cf[0] * cf[2])) / 2 * cf[0]}''')
			user_data[message.from_user.id] = []
		else:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 3 and message.text.lower() == 'q':	
		markup = types.ReplyKeyboardRemove(selective=False)																	
		bot.send_message(message.from_user.id, "Введите удельную теплоёмкость (Дж/кг * °C)", reply_markup=markup)
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 'q':
		markup = types.ReplyKeyboardRemove(selective=False)
		bot.send_message(message.from_user.id, "Введите начальную температуру (°C)", reply_markup=markup)
		local_data.append(float(message.text.lower()))
	elif len(local_data) == 5 and local_data[3] == 'q':
		bot.send_message(message.from_user.id, "Введите конечную  температуру (°C)")
		local_data.append(float(message.text.lower()))
	elif len(local_data) == 6 and local_data[3] == 'q':
			bot.send_message(message.from_user.id, "Введите массу (кг)")
			local_data.append(float(message.text.lower()))	
	elif len(local_data) == 7 and local_data[3] == 'q':
		local_data.append(float(message.text.lower()))
		if int(local_data[4] * (local_data[6] - local_data[5]) * local_data[7]) % 1000 == 0:
			bot.send_message(message.from_user.id, f'''Q = cm(t₂ - t₁)
Q = {int(local_data[4])} * {int(local_data[7])} * ({int(local_data[6])} - {int(local_data[5])})
Q = {int(local_data[4] * (local_data[6] - local_data[5]) * local_data[7])} Дж
Ответом на эту задачу является: {int(local_data[4] * (local_data[6] - local_data[5]) * local_data[7]) // 1000} кДж. (Для перевода в Дж *1000)''')
		else:
			bot.send_message(message.from_user.id, f'''Q = cm(t₂ - t₁)
Q = {int(local_data[4])} * {int(local_data[7])} * ({int(local_data[6])} - {int(local_data[5])})
Q = {int(local_data[4] * (local_data[6] - local_data[5]) * local_data[7])} Дж
Ответом на эту задачу является: {int(local_data[4] * (local_data[6] - local_data[5]) * local_data[7])} Дж.''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 3 and message.text.lower() == 'c':	
		markup = types.ReplyKeyboardRemove(selective=False)
		bot.send_message(message.from_user.id, "Введите количество теплоты (Дж)", reply_markup=markup)
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 'c':
			bot.send_message(message.from_user.id, "Введите начальную температуру (°C)")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 5 and local_data[3] == 'c':
			bot.send_message(message.from_user.id, "Введите конечную  температуру (°C)")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 6 and local_data[3] == 'c':
			bot.send_message(message.from_user.id, "Введите массу (кг)")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 7 and local_data[3] == 'c':
		local_data.append(float(message.text.lower()))
		bot.send_message(message.from_user.id, f'''Q = cm(t₂ - t₁)
c = Q / (m * (t₂ - t₁))
c = {int(local_data[4])} / ({int(local_data[7])} * ({int(local_data[6])} - {int(local_data[5])}))
Ответом на эту задачу является: {round(local_data[4]  / (local_data[6] - local_data[5]) * local_data[7])} (Дж/кг * °C).''')
		user_data[message.from_user.id] = []
	elif len(local_data) == 3 and message.text.lower() == 't₁': 
		markup = types.ReplyKeyboardRemove(selective=False)
		bot.send_message(message.from_user.id, "Введите количество теплоты (Дж)", reply_markup=markup)
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 't₁':
			bot.send_message(message.from_user.id, "Введите удельную теплоёмкость (Дж/кг * °C)")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 5 and local_data[3] == 't₁':
			bot.send_message(message.from_user.id, "Введите конечную  температуру (°C)")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 6 and local_data[3] == 't₁':
			bot.send_message(message.from_user.id, "Введите массу (кг)")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 7 and local_data[3] == 't₁':
		local_data.append(float(message.text.lower()))
		bot.send_message(message.from_user.id, f'''Q = cm(t₂ - t₁)
t₁ = t₂ - (Q / cm)
t₁ = {int(local_data[6])} - ({int(local_data[4])} / {int(local_data[5])}{int(local_data[6])})
Ответом на эту задачу является: {round(local_data[6] - (local_data[4]/(local_data[5] * local_data[6])))} (°C).''')
		user_data[message.from_user.id] = []   
	elif len(local_data) == 3 and message.text.lower() == 't₂': 
		markup = types.ReplyKeyboardRemove(selective=False)
		bot.send_message(message.from_user.id, "Введите количество теплоты (Дж)", reply_markup=markup)
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 't₂':
			bot.send_message(message.from_user.id, "Введите удельную теплоёмкость (Дж/кг * °C)")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 5 and local_data[3] == 't₂':
			bot.send_message(message.from_user.id, "Введите начальную  температуру (°C)")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 6 and local_data[3] == 't₂':
			markup = types.ReplyKeyboardRemove(selective=False)
			bot.send_message(message.from_user.id, "Введите массу (кг)", reply_markup=markup)
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 7 and local_data[3] == 't₂':
		local_data.append(float(message.text.lower()))
		bot.send_message(message.from_user.id, f'''Q = cm(t₂ - t₁)
t₂ = t₁ + (Q / cm)
t₂ = {int(local_data[6])} + ({int(local_data[4])} / {int(local_data[5])}{int(local_data[6])})
Ответом на эту задачу является: {round(local_data[6] - (local_data[4]/(local_data[5] * local_data[6])))} (°C).''')
		user_data[message.from_user.id] = []     
	elif len(local_data) == 3 and message.text.lower() == 'm':	
		markup = types.ReplyKeyboardRemove(selective=False)																	
		bot.send_message(message.from_user.id, "Введите количество теплоты (Дж)", reply_markup=markup)
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 'm':
		markup = types.ReplyKeyboardRemove(selective=False)
		bot.send_message(message.from_user.id, "Введите удельную теплоёмкость (Дж/кг * °C)", reply_markup=markup)
		local_data.append(float(message.text.lower()))
	elif len(local_data) == 5 and local_data[3] == 'm':
		bot.send_message(message.from_user.id, "Введите начальную температуру (°C)")
		local_data.append(float(message.text.lower()))
	elif len(local_data) == 6 and local_data[3] == 'm':
			bot.send_message(message.from_user.id, "Введите конечную  температуру (°C)")
			local_data.append(float(message.text.lower()))	
	elif len(local_data) == 7 and local_data[3] == 'm':
		local_data.append(float(message.text.lower()))
		bot.send_message(message.from_user.id, f'''Q = cm(t₂ - t₁)
m = {int(local_data[4])} / ({int(local_data[5])} * ({int(local_data[7])} - {int(local_data[6])}))
m = {float(local_data[4]) / (float(local_data[5]) * ((float(local_data[7]) - float(local_data[6]))))} кг
Ответом на эту задачу является: {round(float(int(local_data[4]) / (int(local_data[5]) * ((int(local_data[7]) - int(local_data[6]))))), 3)} кг.''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 2 and local_data[1] == 'скорость':
		local_data.append(float(message.text))
		markup = types.ReplyKeyboardMarkup()
		Speed1 = types.KeyboardButton('км/ч')
		Speed2 = types.KeyboardButton('м/с')
		markup.add(Speed1, Speed2)
		# = types.KeyboardButton('t₁')
		# = types.KeyboardButton('t₂')
		# = types.KeyboardButton('m')
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'км/ч':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''км/ч - {speed}
м/с - {speed / 3.6}''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 3 and message.text.lower() == 'м/с':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''км/ч - {speed * 3.6}
м/с - {speed}''')
		user_data[message.from_user.id] = []	

	print(user_data)                                                                                                                                   
bot.infinity_polling(timeout=1080)