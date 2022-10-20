from threading import local
import telebot
from telebot import types
from random import *

bot = telebot.TeleBot('5670990101:AAHCY6UcN3pZC43P5FbVulljTAZVrlo4TWA');
user_data = {}			#creating a dictionary with all user inputs to correct working
#0 - флаг 1-название 2 - столица 3-дата основания 4-население 5-форма правления 6-глава и пост 7 - официальные языки 8 -  валюта 
country_data = {'Россия': ['https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/320px-Flag_of_Russia.svg.png', 'Российская Федерация', 'Москва', '25.12.1991', '147 млн. человек', 'республика', 'Владимир Владимирович Путин, президент РФ (на 2022)', 'русский', 'российский рубль, ₽']}

#start function
@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}, этот бот поможет тебе в решении задач по таким предметам как физика.')

#cat function
@bot.message_handler(commands=['cat'])
def cat(message):
	list_cats = ['https://ferma-biz.ru/wp-content/uploads/2022/08/QPdAc.jpg', 'https://ferma-biz.ru/wp-content/uploads/2022/08/koty-50.jpg', 'https://fydi.ru/wp-content/uploads/2021/08/koty-i-koshki-93.jpg']
	bot.send_photo(message.from_user.id, photo = choice(list_cats))

#help function
@bot.message_handler(commands=['help'])
def help(message):
	markup = types.ReplyKeyboardMarkup() 
	clear_markup1 = types.KeyboardButton('Решение задач') 
	clear_markup2 = types.KeyboardButton('Справочные материалы') 
	markup.add(clear_markup1, clear_markup2)
	bot.send_message(message.from_user.id, f'Список команд:\n  /clear -  очищает актуальный кэш бота и возвращает к началу.\n /cat -  отправляет фотографию котика, чтобы скрасить тяжелые будни)\n\n   {message.from_user.first_name}, напиши "решение задач" или "справочные материалы"', reply_markup=markup)

#clear function
@bot.message_handler(commands=['clear'])
def help(message):
	global user_data
	user_data[message.from_user.id] = []
	markup = types.ReplyKeyboardMarkup() 
	clear_markup1 = types.KeyboardButton('Решение задач') 
	markup.add(clear_markup1)
	bot.send_message(message.from_user.id, 'История очищена!', reply_markup=markup)
	
#main function
@bot.message_handler(content_types=['text'])			
def main(message):
	global user_data			#setting local data to simplify the program
	global country_data
	print(user_data)
	if message.from_user.id not in user_data:
		user_data[message.from_user.id] = []
	local_data = user_data[message.from_user.id]
	if len(local_data) == 0:			#main branch
		if message.text.lower() == 'решение задач':
			markup = types.ReplyKeyboardMarkup()    
			subjbut1 = types.KeyboardButton('Физика') 
			subjbut2 = types.KeyboardButton('Информатика') 
			markup.add(subjbut1)
			bot.send_message(message.from_user.id, "Выберите предмет", reply_markup=markup)
			local_data.append(message.text.lower())
		if message.text.lower() == 'справочные материалы':
			markup = types.ReplyKeyboardMarkup()    
			subjbut1 = types.KeyboardButton('География')
			markup.add(subjbut1)
			bot.send_message(message.from_user.id, "Выберите предмет", reply_markup=markup)
			local_data.append(message.text.lower())
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, для помощи напиши команду  /help')

			
	elif len(local_data) == 1 and local_data[0] == 'справочные материалы':
		bot.send_message(message.from_user.id, 'Введи название страны, что бы получить основную информацию о ней:')
		local_data.append(message.text.lower())

	elif len(local_data) == 2 and local_data[0] == 'справочные материалы':
		if message.text.title() in country_data:
			local_data.append(message.text.lower())
			text = f"---{country_data[str(local_data[2].title())][1]}---\n ‣Столица: {country_data[str(local_data[2].title())][2]}\n  ‣Дата основания: {country_data[str(local_data[2].title())][3]}\n ‣Численность населения(млн. чел): {country_data[str(local_data[2].title())][4]}\n ‣Форма правления: {country_data[str(local_data[2].title())][5]}\n ‣Глава государства и должность: {country_data[str(local_data[2].title())][6]}\n ‣Официльный(е) язык(и): {country_data[str(local_data[2].title())][7]}\n ‣Валюта: {country_data[str(local_data[2].title())][8]}\n"
			bot.send_photo(message.from_user.id, photo=country_data[local_data[2].title()][0], caption=text)
			user_data[message.from_user.id] = []    
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, видимо в нашей базе ещё нет этой страны.')

	#0 - флаг 1-название 2-дата основания 3-население 4-форма правления 5-глава и пост




	elif len(local_data) == 1 and local_data[0] == 'решение задач':			#subject branch
		if message.text.lower() == 'физика':
			markup = types.ReplyKeyboardMarkup()
			physchapter1 = types.KeyboardButton('Термодинамика')
			markup.add(physchapter1)
			bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
			local_data.append(message.text.lower())
		elif message.text.lower() == 'информатика':
			bot.send_message(message.from_user.id, "В разработке")
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, выбери нужный тебе предмет:')



	elif len(local_data) == 2:			#chapter branch
		if message.text.lower() == 'термодинамика':
			markup = types.ReplyKeyboardMarkup()
			PhysicsThermodynamics1 = types.KeyboardButton('Количество теплоты')
			PhysicsThermodynamics2 = types.KeyboardButton('Удельная теплоёмкость')
			PhysicsThermodynamics3 = types.KeyboardButton('Начальная температура')
			PhysicsThermodynamics4 = types.KeyboardButton('Конечная температура')
			markup.add(PhysicsThermodynamics1, PhysicsThermodynamics2, PhysicsThermodynamics3, PhysicsThermodynamics4)
			bot.send_message(message.from_user.id, "Выберите неизвестное", reply_markup=markup)
			local_data.append(message.text.lower())
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, выбери нужный тебе раздел:')



	elif len(local_data) == 3 and message.text.lower() == 'количество теплоты':																											#start of thermodynamic(1)
		bot.send_message(message.from_user.id, "Введите удельную теплоёмкость (Дж/кг * °C)")
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 'количество теплоты':
		if int(message.text) > 0:
			bot.send_message(message.from_user.id, "Введите начальную температуру (°C)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 5 and local_data[3] == 'количество теплоты':
		if int(message.text) >= 0:
			bot.send_message(message.from_user.id, "Введите конечную  температуру (°C)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 6 and local_data[3] == 'количество теплоты':
		if int(message.text) >= 0:
			bot.send_message(message.from_user.id, "Введите массу (кг)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 7 and local_data[3] == 'количество теплоты':
		local_data.append(float(message.text.lower()))
		if int(local_data[4] * (local_data[6] - local_data[5]) * local_data[7]) % 1000 == 0:
			bot.send_message(message.from_user.id, f'Ответом на эту задачу является: {int(local_data[4] * (local_data[6] - local_data[5]) * local_data[7]) // 1000} кДж. (Для перевода в Дж *1000)')
		else:
			bot.send_message(message.from_user.id, f'Ответом на эту задачу является: {round(local_data[4] * (local_data[6] - local_data[5]) * local_data[7])} Дж.')
		user_data[message.from_user.id] = []																																		#end of thermodynamic(1)



	elif len(local_data) == 3 and (message.text.lower() == 'удельная теплоемкость' or message.text.lower() == 'удельная теплоёмкость'):																											#start of thermodynamic(2)
		bot.send_message(message.from_user.id, "Введите количество теплоты (Дж)")
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and (local_data[3] == 'удельная теплоемкость' or local_data[3] == 'удельная теплоёмкость'):
		if int(message.text) > 0:
			bot.send_message(message.from_user.id, "Введите начальную температуру (°C)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 5 and (local_data[3] == 'удельная теплоемкость' or local_data[3] == 'удельная теплоёмкость'):
		if int(message.text) >= 0:
			bot.send_message(message.from_user.id, "Введите конечную  температуру (°C)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 6 and (local_data[3] == 'удельная теплоемкость' or local_data[3] == 'удельная теплоёмкость'):
		if int(message.text) >= 0:
			bot.send_message(message.from_user.id, "Введите массу (кг)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 7 and (local_data[3] == 'удельная теплоемкость' or local_data[3] == 'удельная теплоёмкость'):
		local_data.append(float(message.text.lower()))
		bot.send_message(message.from_user.id, f'Ответом на эту задачу является: {round(local_data[4]  / (local_data[6] - local_data[5]) * local_data[7])} (Дж/кг * °C).')
		user_data[message.from_user.id] = []																																		#end of thermodynamic(2)



	elif len(local_data) == 3 and message.text.lower() == 'начальная температура':                                                                                                         #start of thermodynamic(3)
		bot.send_message(message.from_user.id, "Введите количество теплоты (Дж)")
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 'начальная температура':
		if int(message.text) > 0:
			bot.send_message(message.from_user.id, "Введите удельную теплоёмкость (Дж/кг * °C)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 5 and local_data[3] == 'начальная температура':
		if int(message.text) >= 0:
			bot.send_message(message.from_user.id, "Введите конечную  температуру (°C)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 6 and local_data[3] == 'начальная температура':
		if int(message.text) >= 0:
			bot.send_message(message.from_user.id, "Введите массу (кг)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 7 and local_data[3] == 'начальная температура':
		local_data.append(float(message.text.lower()))
		bot.send_message(message.from_user.id, f'Ответом на эту задачу является: {round(local_data[6] - (local_data[4]/(local_data[5] * local_data[6])))} (°C).')
		user_data[message.from_user.id] = []                                                                                                                                        #end of thermodynamic(3)



	elif len(local_data) == 3 and message.text.lower() == 'конечная температура':                                                                                                         #start of thermodynamic(4)
		bot.send_message(message.from_user.id, "Введите количество теплоты (Дж)")
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 'конечная температура':
		if int(message.text) > 0:
			bot.send_message(message.from_user.id, "Введите удельную теплоёмкость (Дж/кг * °C)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 5 and local_data[3] == 'конечная температура':
		if int(message.text) >= 0:
			bot.send_message(message.from_user.id, "Введите начальную  температуру (°C)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 6 and local_data[3] == 'конечная температура':
		if int(message.text) >= 0:
			bot.send_message(message.from_user.id, "Введите массу (кг)")
			local_data.append(float(message.text.lower()))
		else:
			bot.send_message(message.from_user.id, "Введите корректное значение, если нужна помощь - /help")
	elif len(local_data) == 7 and local_data[3] == 'конечная температура':
		local_data.append(float(message.text.lower()))
		bot.send_message(message.from_user.id, f'Ответом на эту задачу является: {round(local_data[6] + (local_data[4]/(local_data[5] * local_data[7])))} (°C).')
		user_data[message.from_user.id] = []                                                                                                                                        #end of thermodynamic(4)


	print(user_data)

bot.infinity_polling(timeout=1080)                                                                                                                               #end of thermodynamic(3)
