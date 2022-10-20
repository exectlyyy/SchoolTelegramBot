from threading import local
import telebot
from telebot import types

bot = telebot.TeleBot('5670990101:AAHCY6UcN3pZC43P5FbVulljTAZVrlo4TWA');
user_data = {}

@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}, этот бот поможет тебе в решении задач по таким предметам как физика.')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, 'Проверка комманды /help, написать про предметы')

@bot.message_handler(content_types=['text'])			
def main(message):
	global user_data
	print(user_data)
	if message.from_user.id not in user_data:
		user_data[message.from_user.id] = []
	local_data = user_data[message.from_user.id]
	
	if len(local_data) == 0:
		if message.text.lower() == 'предмет':
			markup = types.ReplyKeyboardMarkup()    
			subjbut1 = types.KeyboardButton('Физика') 			
			markup.add(subjbut1)
			bot.send_message(message.from_user.id, "Выберите предмет", reply_markup=markup)
			local_data.append(message.text.lower())
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, для помощи напиши команду  /help')
	elif len(local_data) == 1:
		if message.text.lower() == 'физика':
			markup = types.ReplyKeyboardMarkup()
			physchapter1 = types.KeyboardButton('Термодинамика')
			markup.add(physchapter1)
			bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
			local_data.append(message.text.lower())
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, выбери нужный тебе предмет:')
	elif len(local_data) == 2:
		if message.text.lower() == 'термодинамика':
			markup = types.ReplyKeyboardMarkup()
			pt1 = types.KeyboardButton('Количество теплоты')
			markup.add(pt1)
			bot.send_message(message.from_user.id, "Выберите неизвестное", reply_markup=markup)
			local_data.append(message.text.lower())
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, выбери нужный тебе раздел:')
	elif len(local_data) == 3:
		if message.text.lower() == 'количество теплоты':
			bot.send_message(message.from_user.id, "Введите удельную теплоёмкость (Дж/кг * °C)")
			local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 'количество теплоты':
		if int(message.text) > 0:
			bot.send_message(message.from_user.id, "Введите начальную температуру")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 5 and local_data[3] == 'количество теплоты':
		if int(message.text) > 0:
			bot.send_message(message.from_user.id, "Введите конечную  температуру")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 6 and local_data[3] == 'количество теплоты':
		if int(message.text) > 0:
			bot.send_message(message.from_user.id, "Введите массу")
			local_data.append(float(message.text.lower()))
	elif len(local_data) == 7 and local_data[3] == 'количество теплоты':
		local_data.append(float(message.text.lower()))
		bot.send_message(message.from_user.id, f'Ответом на эту задачу является: {int(local_data[4] * (local_data[6] - local_data[5]) * local_data[7])} джоулей.')
		user_data[message.from_user.id] = []

	print(user_data)

bot.infinity_polling()