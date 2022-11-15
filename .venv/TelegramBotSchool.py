import telebot

from telebot import types
from random import *
from math import sqrt

bot = telebot.TeleBot('5670990101:AAHCY6UcN3pZC43P5FbVulljTAZVrlo4TWA');
user_data = {}	
ideas_data = {}	
country_data = {'Россия': ['https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/320px-Flag_of_Russia.svg.png', 'Российская Федерация', 'Москва', '25.12.1991', '147 млн. человек', 'республика', 'Владимир Владимирович Путин, президент РФ (на 2022)', 'русский', 'российский рубль, ₽ (RUB)', 'https://ru.wikipedia.org/wiki/Россия'], 
				'Рф': ['https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/320px-Flag_of_Russia.svg.png', 'Российская Федерация', 'Москва', '25.12.1991', '147 млн. человек', 'республика', 'Владимир Владимирович Путин, президент РФ (на 2022)', 'русский', 'российский рубль, ₽ (RUB)', 'https://ru.wikipedia.org/wiki/Россия'], 
				'Япония': ['https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/320px-Flag_of_Japan.svg.png', 'Япония', 'Токио', '11.02.660 до н.э.', '125 млн. человек', 'конституционная монархия', 'Нарухито, император\n Фумио Кисида, премьер-министр (на 2022)', 'японский', 'японская иена, ¥ (JPY)', 'https://ru.wikipedia.org/wiki/Япония'],
				'Франция': ['https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_France_%281794–1815%2C_1830–1974%2C_2020–present%29.svg/160px-Flag_of_France_%281794–1815%2C_1830–1974%2C_2020–present%29.svg.png', 'Французская Республика', 'Париж', '04.10.1958', '68 млн. чел', 'президентско-парламентская республика', 'Эмманюэль Макрон, президент (на 2022)', 'французкий', 'евро, € (EUR)', 'https://ru.wikipedia.org/wiki/Франция'],
				'Кндр': ['https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Flag_of_North_Korea.svg/160px-Flag_of_North_Korea.svg.png', 'Корейская Народно-Демократическая Республика', 'Пхеньян', '09.09.1948', '25,9 млн. чел.', 'однопартийная парламентская республика', 'Ким Чен Ын, председатель гос. совета (на 2022)', 'корейский', 'северокорейская вона (KPW)', 'https://ru.wikipedia.org/wiki/Корейская_Народно-Демократическая_Республика'],
				'Оаэ': ['https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_United_Arab_Emirates.svg/160px-Flag_of_the_United_Arab_Emirates.svg.png', 'Объединённые Арабские Эмираты', 'Абу-Даби', '02.12.1971 (независимость)', '10,2 млн. чел.', 'абсолютная монархия', 'Мухаммад ибн Заид Аль Нахайян, президент (на 2022)', 'арабский', 'дирхам ОАЭ (AED)', 'https://ru.wikipedia.org/wiki/Объединённые_Арабские_Эмираты'],
				'Объединённые Арабские Эмираты': ['https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_United_Arab_Emirates.svg/160px-Flag_of_the_United_Arab_Emirates.svg.png', 'Объединённые Арабские Эмираты', 'Абу-Даби', '02.12.1971 (независимость)', '10,2 млн. чел.', 'абсолютная монархия', 'Мухаммад ибн Заид Аль Нахайян, президент (на 2022)', 'арабский', 'дирхам ОАЭ (AED)', 'https://ru.wikipedia.org/wiki/Объединённые_Арабские_Эмираты'],
				'Объединенные Арабские Эмираты': ['https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Flag_of_the_United_Arab_Emirates.svg/160px-Flag_of_the_United_Arab_Emirates.svg.png', 'Объединённые Арабские Эмираты', 'Абу-Даби', '02.12.1971 (независимость)', '10,2 млн. чел.', 'абсолютная монархия', 'Мухаммад ибн Заид Аль Нахайян, президент (на 2022)', 'арабский', 'дирхам ОАЭ (AED)', 'https://ru.wikipedia.org/wiki/Объединённые_Арабские_Эмираты'],
				'Норвегия': ['https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Norway.svg/160px-Flag_of_Norway.svg.png', 'Королевство Норвегия',  'Осло', '15.12.1899', '5,5 млн. чел.', 'конституционная монархия', 'Харальд V, король\n Йонас Гар Стёре. премьер-министр (на 2022)', 'норвежский', 'норвежская крона (NOK)', 'https://ru.wikipedia.org/wiki/Норвегия']}

@bot.message_handler(commands=['start'])			
def greetings(message):			#ФУНКЦИЯ СТАРТ	
	markup = types.ReplyKeyboardMarkup()    
	HelpMarkup = types.KeyboardButton('/help')  
	markup.add(HelpMarkup)
	bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}, этот бот поможет тебе в решении задач по таким предметам как физика.', reply_markup=markup)

@bot.message_handler(commands=['idea'])			
def idea(message):			#ФУНКЦИЯ ИДЕЙ
	markup = types.ReplyKeyboardRemove(selective=False)
	bot.send_message(message.from_user.id, f'Напиши сообщение, начинающееся на слово идея и оно будет передано моим создателям.', reply_markup=markup)

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
	bot.send_message(message.from_user.id, f'''Список команд:
 /clear -  очищает актуальный кэш бота и возвращает к началу.
 /cat -  отправляет фотографию котика, чтобы скрасить тяжелые будни)
 /idea - что бы предложить идею создателям бота, возможно она будет реализована в дальшейшем.
	
{message.from_user.first_name}, напиши "решение задач", "конвертер величин" или "справочные материалы"''', reply_markup=markup)

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

def First_message(message, local_data):
	if message.text.lower()[:4] == 'идея':
		markup = types.ReplyKeyboardRemove(selective=False)
		bot.send_message(message.from_user.id, "Спасибо за идею!", reply_markup=markup)	
		ideas_data[message.from_user.id].append(message.text.lower()[5:])																						#ОСНОВНАЯ ВЕТКА (РЕШЕНИЕ ЗАДАЧ\СПРАВОЧНЫЕ МАТЕРИАЛЫ)
	elif message.text.lower() == 'решение задач':
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

def int_round(x):
	if x % 1 == 0:
		return int(x)
	else:
		return x

def DFF(message):
	answer = ''
	s = [str(message)[i] for i in range(len(message))]
	for i in range(len(s)):
		if s[i] not in '1234567890-,.':
			return None
		if s[i] == ',':
			s[i] = '.'
		answer += s[i]
	for i in range(len(answer)):
		if answer[i] == '.':
			return float(answer)	
	return int(answer)
	
@bot.message_handler(content_types=['text'])			
def main(message):
	global user_data			
	global country_data	
	global ideas_data	
	if message.from_user.id not in ideas_data: 																			#СОЗДАЕТ ПЕРЕМЕННУЮ, ЗАПОМИНАЮЩУЮ СООБЩЕНИЯ
		ideas_data[message.from_user.id] = [message.from_user.first_name]																				#СОЗДАЕТ ПЕРЕМЕННУЮ, ЗАПОМИНАЮЩУЮ СООБЩЕНИЯ
	if message.from_user.id not in user_data: 																			#СОЗДАЕТ ПЕРЕМЕННУЮ, ЗАПОМИНАЮЩУЮ СООБЩЕНИЯ
		user_data[message.from_user.id] = []
	local_data = user_data[message.from_user.id]
	if len(local_data) == 0:
		First_message(message, local_data)
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
			bot.send_message(message.from_user.id, f'Более подробную информацию ты можешь узнать здесь {country_data[str(local_data[2].title())][9]}')
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
		if len(cf) == 3:
			cf[0] = cf[0].replace(',', '.', 1)
			cf[1] = cf[1].replace(',', '.', 1)
			cf[2] = cf[2].replace(',', '.', 1)
			a = float(cf[0])
			b = float(cf[1])
			c = float(cf[2])
			D = (b ** 2) - (4 * a * c)
			a = int_round(a)
			b = int_round(b)
			c = int_round(c)
			D = int_round(D)
			if a == 0:
					bot.send_message(message.from_user.id, f'''Уравнение не является квадратным, так как а = 0''')
			elif D > 0:
				if a > 0:
					if not b <= 0:
						if not c <= 0:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²+{b}x+{c}=0
D = {b}² - 4 * {a} * {c} = {D}
x₁ = (-({b}) + √{D}) / (2 * {a}) = {(-(b) + sqrt(D)) / (2 * a)}
x₂ = (-({b}) - √{D}) / (2 * {a}) = {(-(b) - sqrt(D)) / (2 * a)}''')
						else:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²+{b}x{c}=0
D = {b}² + 4 * {a} * {str(c)[1:]} = {D}
x₁ = (-({b}) + √{D}) / (2 * {a}) = {(-(b) + sqrt(D)) / (2 * a)}
x₂ = (-({b}) - √{D}) / (2 * {a}) = {(-(b) - sqrt(D)) / (2 * a)}''')
					else:
						if not c <= 0:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²{b}x+{c}=0
D = ({b})² - 4 * {a} * {c} = {D}
x₁ = ({str(b)[1:]} + √{D}) / (2 * {a}) = {(-(b) + sqrt(D)) / (2 * a)}
x₂ = ({str(b)[1:]} - √{D}) / (2 * {a}) = {(-(b) - sqrt(D)) / (2 * a)}''')
						else:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²{b}x+{c}=0
D = ({b})² - 4 * {a} * {c} = {D}
x₁ = ({str(b)[1:]} + √{D}) / (2 * {a}) = {(-(b) + sqrt(D)) / (2 * a)}
x₂ = ({str(b)[1:]} - √{D}) / (2 * {a}) = {(-(b) - sqrt(D)) / (2 * a)}''')
				else:
					if not b <= 0:
						if not c <= 0:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²+{b}x+{c}=0
D = {b}² + 4 * {str(a)[1:]} * {c} = {D}
x₁ = (-({b}) + √{D}) / -(2 * {str(a)[1:]}) = {(-(b) + sqrt(D)) / (2 * a)}
x₂ = (-({b}) - √{D}) / -(2 * {str(a)[1:]}) = {(-(b) - sqrt(D)) / (2 * a)}''')
						else:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²+{b}x{c}=0
D = {b}² - 4 * {str(a)[1:]} * {str(c)[1:]} = {D}
x₁ = (-({b}) + √{D}) / -(2 * {str(a)[1:]}) = {(-(b) + sqrt(D)) / (2 * a)}
x₂ = (-({b}) - √{D}) / -(2 * {str(a)[1:]}) = {(-(b) - sqrt(D)) / (2 * a)}''')
					else:
						if not c <= 0:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²{b}x+{c}=0
D = ({b})² + 4 * {str(a)[1:]} * {c} = {D}
x₁ = ({str(b)[1:]} + √{D}) / -(2 * {str(a)[1:]}) = {(-(b) + sqrt(D)) / (2 * a)}
x₂ = ({str(b)[1:]} - √{D}) / -(2 * {str(a)[1:]}) = {(-(b) - sqrt(D)) / (2 * a)}''')
						else:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²{b}x+{c}=0
D = ({b})² - 4 * {str(a)[1:]} * {str(c)[1:]} = {D}
x₁ = ({str(b)[1:]} + √{D}) / -(2 * {str(a)[1:]}) = {(-(b) + sqrt(D)) / (2 * a)}
x₂ = ({str(b)[1:]} - √{D}) / -(2 * {str(a)[1:]}) = {(-(b) - sqrt(D)) / (2 * a)}''')	
			elif D == 0:			#дописать
				if a > 0:
					if not b <= 0:
						if not c <= 0:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²+{b}x+{c}=0
D = {b}² - 4 * {a} * {c} = {D}
x = (-({b}) + √{D}) / (2 * {a}) = {(-(b) + sqrt(D)) / (2 * a)}
''')
						else:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²+{b}x{c}=0
D = {b}² + 4 * {a} * {str(c)[1:]} = {D}
x = (-({b}) + √{D}) / (2 * {a}) = {(-(b) + sqrt(D)) / (2 * a)}
''')
					else:
						if not c <= 0:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²{b}x+{c}=0
D = ({b})² - 4 * {a} * {c} = {D}
x = ({str(b)[1:]} + √{D}) / (2 * {a}) = {(-(b) + sqrt(D)) / (2 * a)}
''')
						else:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²{b}x+{c}=0
D = ({b})² - 4 * {a} * {c} = {D}
x = ({str(b)[1:]} + √{D}) / (2 * {a}) = {(-(b) + sqrt(D)) / (2 * a)}
''')
				else:
					if not b <= 0:
						if not c <= 0:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²+{b}x+{c}=0
D = {b}² + 4 * {str(a)[1:]} * {c} = {D}
x = (-({b}) + √{D}) / -(2 * {str(a)[1:]}) = {(-(b) + sqrt(D)) / (2 * a)}
''')
						else:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²+{b}x{c}=0
D = {b}² - 4 * {str(a)[1:]} * {str(c)[1:]} = {D}
x = (-({b}) + √{D}) / -(2 * {str(a)[1:]}) = {(-(b) + sqrt(D)) / (2 * a)}
''')
					else:
						if not c <= 0:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²{b}x+{c}=0
D = ({b})² + 4 * {str(a)[1:]} * {c} = {D}
x = ({str(b)[1:]} + √{D}) / -(2 * {str(a)[1:]}) = {(-(b) + sqrt(D)) / (2 * a)}
''')
						else:
							bot.send_message(message.from_user.id, f'''Уравнение {a}x²{b}x+{c}=0
D = ({b})² - 4 * {str(a)[1:]} * {str(c)[1:]} = {D}
x = ({str(b)[1:]} + √{D}) / -(2 * {str(a)[1:]}) = {(-(b) + sqrt(D)) / (2 * a)}
''')	
			else:
				bot.send_message(message.from_user.id, f'''Уравнение не имеет решений, так как дискриминат меньше нуля''')
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
		v1 = DFF(message.text.lower())
		if v1 != None:
			if v1 >= 0:
				local_data.append(v1)
			else:
				bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
		elif v1 == None:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 5 and local_data[3] == 'q':
		bot.send_message(message.from_user.id, "Введите конечную  температуру (°C)")
		v1 = DFF(message.text.lower())
		if v1 != None:
			local_data.append(v1)
		elif v1 == None:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 6 and local_data[3] == 'q':
		bot.send_message(message.from_user.id, "Введите массу (кг)")
		v1 = DFF(message.text.lower())
		if v1 != None:
			if v1 >= 0:
				local_data.append(v1)
			else:
				bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
		elif v1 == None:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 7 and local_data[3] == 'q':
		v1 = DFF(message.text.lower())
		if v1 != None:
			local_data.append(v1)
			if int(local_data[4] * (local_data[6] - local_data[5]) * local_data[7]) % 1000 == 0:
				bot.send_message(message.from_user.id, f'''Q = cm(t₂ - t₁)
Q = {local_data[4]} * {local_data[7]} * ({local_data[6]} - {local_data[5]})
Q = {int(local_data[4] * (local_data[6] - local_data[5]) * local_data[7])} Дж
Ответом на эту задачу является: {(local_data[4] * (local_data[6] - local_data[5]) * local_data[7]) // 1000} кДж. (Для перевода в Дж *1000)''')
			else:
				bot.send_message(message.from_user.id, f'''Q = cm(t₂ - t₁)
Q = {local_data[4]} * {local_data[7]} * ({local_data[6]} - {local_data[5]})
Q = {(local_data[4] * (local_data[6] - local_data[5]) * local_data[7])} Дж
Ответом на эту задачу является: {local_data[4] * (local_data[6] - local_data[5]) * local_data[7]} Дж.''')
			user_data[message.from_user.id] = []
		elif v1 == None:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')	
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
		Speed3 = types.KeyboardButton('км/мин')
		Speed4 = types.KeyboardButton('м/мин')
		markup.add(Speed1, Speed2, Speed3, Speed4)
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'км/ч':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''км/ч - {speed}
км/мин - {speed / 60}
м/с - {speed / 3.6}
м/мин - {speed / 3.6 * 60}
''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 3 and message.text.lower() == 'м/с':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''км/ч - {speed * 3.6}
км/мин - {speed * 3.6 / 60}
м/с - {speed}
м/мин - {speed * 60}
''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 3 and message.text.lower() == 'км/мин':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''км/ч - {speed / 60}
км/мин - {speed}
м/с - {speed / 60 / 3.6}
м/мин - {speed / 3.6}
''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 3 and message.text.lower() == 'м/мин':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''км/ч - {speed * 3.6 * 60}
км/мин - {speed * 3.6}
м/с - {speed * 60}
м/мин - {speed}
''')
		user_data[message.from_user.id] = []
	print(user_data)      
	print(ideas_data)                                                                                                                             
bot.infinity_polling(timeout=1080)