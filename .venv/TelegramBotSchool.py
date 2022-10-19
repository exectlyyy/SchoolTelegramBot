import telebot
from telebot import types

bot = telebot.TeleBot('5670990101:AAHCY6UcN3pZC43P5FbVulljTAZVrlo4TWA');

@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.from_user.id, 'Приветственное сообщение, попросить написать /help')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, 'Проверка комманды /help, написать про предметы')



@bot.message_handler(content_types=['text'])			
def main(message):
	if message.text == 'Предмет':
		markup = types.ReplyKeyboardMarkup()    
		subjbut1 = types.KeyboardButton('Физика') 			
		markup.add(subjbut1)
		bot.send_message(message.from_user.id, "Выберите предмет", reply_markup=markup)
	if message.text == 'Физика':
		markup = types.ReplyKeyboardMarkup()
		physchapter1 = types.KeyboardButton('Термодинамика')
		markup.add(physchapter1)
		bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
	if message.text == 'Термодинамика':
		markup = types.ReplyKeyboardMarkup()
		pt1 = types.KeyboardButton('Количество теплоты')
		markup.add(pt1)
		bot.send_message(message.from_user.id, "Выберите неизвестное", reply_markup=markup)
	if message.text == 'Количество теплоты':
		bot.send_message(message.from_user.id, "Введите удельную теплоёмкость (Дж/кг * °C)")
		ptc = int(message.text)
		bot.send_message(message.from_user.id, "Введите начальную температуру")
		ptt1 = int(message.text)
		bot.send_message(message.from_user.id, "Введите конечную")
		ptt2 = int(message.text)
		bot.send_message(message.from_user.id, "Введите массу")
		ptm = int(message.text)
		bot.send_message(message.from_user.id, ptm * ptc * (ptt2 - ptt1))
		

bot.infinity_polling()