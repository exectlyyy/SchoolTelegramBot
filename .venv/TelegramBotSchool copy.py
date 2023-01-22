import telebot

from telebot import types
from random import *
from math import *

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
				'Норвегия': ['https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Norway.svg/160px-Flag_of_Norway.svg.png', 'Королевство Норвегия',  'Осло', '15.12.1899', '5,5 млн. чел.', 'конституционная монархия', 'Харальд V, король\n Йонас Гар Стёре. премьер-министр (на 2022)', 'норвежский', 'норвежская крона (NOK)', 'https://ru.wikipedia.org/wiki/Норвегия'],
				'Испания': ['https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Bandera_de_España.svg/320px-Bandera_de_España.svg.png', 'Королевство Испания', 'Мадрид', '1479', '47,5 млн. чел.', 'конституционная монархия', 'Филипп VI, король', 'испанский', 'евро, EUR', 'https://ru.wikipedia.org/wiki/Испания'],
				'Португалия': ['https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/320px-Flag_of_Portugal.svg.png', 'Португальская республика', 'Лиссабон', '26.07.1139 основание. 03.12.1643 - незамисимость', '10 млн. чел.', 'президенстко-парламентская республика', 'Марселу Ребелу ди Соза, президент', 'Португальский', 'евро, EUR', 'https://ru.wikipedia.org/wiki/Португалия'],
				'Финляндия': ['https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Finland.svg/1920px-Flag_of_Finland.svg.png', 'Финляндская Республика', 'Хельсинки', '~1171 основание. 06.12.1917 - незамисимость', '5,5 млн. чел.', 'парламентская республика', 'Саули Ниинистё, президент', 'Финский, шведский', 'евро, EUR', 'https://ru.wikipedia.org/wiki/Финляндия'],
				'Германия': ['https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/1920px-Flag_of_Germany.svg.png', 'Федеративная Республика Германия', 'Берлин', '~800 основание. 23.05.1949 - незамисимость', '83 млн. чел.', 'федеративная парламентская республика', 'Франк-Вальтер Штайнмайер, президент', 'Немецкий', 'евро, EUR', 'https://ru.wikipedia.org/wiki/Германия'],
				'Кипр': ['https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Cyprus.svg/1024px-Flag_of_Cyprus.svg.png', 'Республика Кипр', 'Южная Никосия', '~965 основание. 16.08.1960 - незамисимость', '1,2 млн. чел.', 'президентская республика', 'Никос Анастасиадис, президент', 'Греческий', 'евро, EUR', 'https://ru.wikipedia.org/wiki/Республика_Кипр'],
				'Турецкая Республика Северного Кипра': ['https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Flag_of_the_Turkish_Republic_of_Northern_Cyprus.svg/1024px-Flag_of_the_Turkish_Republic_of_Northern_Cyprus.svg.png', 'ТРСК', 'Северная Никосия', '~07.1974 основание. 15.11.1983 - незамисимость', '382 тыс. чел.', 'президентская республика', 'Эрсин Татар, президент', 'Турецкий', 'турецкая лира, TRY', 'https://ru.wikipedia.org/wiki/Турецкая_Республика_Северного_Кипра'],
				'Дания': ['https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/800px-Flag_of_Denmark.svg.png', 'Королевство Дания', 'Копенгаген', '~8 век основание', '5,8 млн. чел.', 'конституционная монархия', 'Маргрете II, королева', 'Датский', 'датская крона, DKK', 'https://ru.wikipedia.org/wiki/Дания']}

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
	clear_markup2 = types.KeyboardButton('Разное') 
	clear_markup3 = types.KeyboardButton('Конвертер величин') 
	markup.add(clear_markup1, clear_markup2, clear_markup3)
	bot.send_message(message.from_user.id, f'''Список команд:
 /clear -  очищает актуальный кэш бота и возвращает к началу.
 /cat -  отправляет фотографию котика, чтобы скрасить тяжелые будни)
 /idea - что бы предложить идею создателям бота, возможно она будет реализована в дальшейшем.
	
{message.from_user.first_name}, напиши "решение задач", "конвертер величин" или "справочные материалы"''', reply_markup=markup)

def pifagor(x):
    l = x.split(' ')
    if '-' in l:
        index = l.index('-')
        if index == 2:
            a = int(l[0])
            b = int(l[1])
            c = sqrt((a ** 2) + (b ** 2))
            return c
        elif index == 1:
            c = int(l[2])
            a = int(l[0])
            b = sqrt((c ** 2) - (a ** 2))
            return b
        elif index == 0:
            c = int(l[2])
            b = int(l[1])
            a = sqrt((c ** 2) - (b ** 2))
            return a
    else:
        return None


def Trygonometry(x):
	if x[-1] != 'r':
		if x[0:3] == 'sin' and x[3:].isdigit():
			return sin(radians(int(x[3:])))
		if x[0:3] == 'cos' and x[3:].isdigit():
			return cos(radians(int(x[3:])))
		if x[0:2] == 'tg' and x[2:].isdigit():
			return tan(radians(int(x[2:])))
		if x[0:3] == 'ctg' and x[3:].isdigit():
			return 1 / tan(radians(int(x[3:])))
		return None
	else:
		if x[0:3] == 'sin' and x[3:-1].isdigit():
			return sin(int(x[3:-1]))
		if x[0:3] == 'cos' and x[3:-1].isdigit():
			return cos(int(x[3:-1]))
		if x[0:2] == 'tg' and x[2:-1].isdigit():
			return tan(int(x[2:-1]))
		if x[0:3] == 'ctg' and x[3:-1].isdigit():
			return 1 / tan(int(x[3:-1]))
		return None
		
@bot.message_handler(commands=['clear'])
def clear(message):				#ФУНКЦИЯ ОЧИСТКИ
	global user_data
	user_data[message.from_user.id] = []
	markup = types.ReplyKeyboardMarkup() 
	clear_markup1 = types.KeyboardButton('Решение задач') 
	clear_markup2 = types.KeyboardButton('Разное') 
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
	elif message.text.lower() == 'разное':
		markup = types.ReplyKeyboardMarkup()    
		SubjectButton1 = types.KeyboardButton('География')
		SubjectButton2 = types.KeyboardButton('Математика')
		SubjectButton3 = types.KeyboardButton('Перевод систем счисления')
		markup.add(SubjectButton1, SubjectButton2, SubjectButton3)
		bot.send_message(message.from_user.id, "Выберите предмет", reply_markup=markup)
		local_data.append(message.text.lower())
	elif message.text.lower() == 'конвертер величин':	
		markup = types.ReplyKeyboardMarkup()    
		TypeButton1 = types.KeyboardButton('Скорость')
		TypeButton2 = types.KeyboardButton('Длина')
		TypeButton3 = types.KeyboardButton('Время')
		TypeButton4 = types.KeyboardButton('Данные')
		TypeButton5 = types.KeyboardButton('Масса')
		TypeButton6 = types.KeyboardButton('Объем')
		TypeButton7 = types.KeyboardButton('Температура')
		TypeButton8 = types.KeyboardButton('Энергия')
		TypeButton9 = types.KeyboardButton('Площадь')
		TypeButton10 = types.KeyboardButton('Мощность')
		TypeButton11 = types.KeyboardButton('Давление')
		TypeButton12 = types.KeyboardButton('Угол')
		markup.add(TypeButton1, TypeButton2, TypeButton3, TypeButton4, TypeButton5, TypeButton6, TypeButton7, TypeButton8, TypeButton9, TypeButton10, TypeButton11, TypeButton12)
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
	if message != '-':
		answer = ''
		s = [str(message)[i] for i in range(len(str(message)))]
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
	return None

def burn(s):
	l = s.split()
	print(l)
	if len(l)!= 3:
		return None
	if l[0] == '-':
		a = DFF(DFF(l[1]) * DFF(l[2]))
		if a % 1000 == 0:
			return f'Ваш ответ Q = q * m = {DFF(l[1])} * {DFF(l[2])} = {a // 1000} КДж'
		return f'Ваш ответ Q = q * m = {DFF(l[1])} * {DFF(l[2])} = {a} Дж'
	if l[1] == '-':
		a = DFF(DFF(l[0]) / DFF(l[2]))
		return f'Ваш ответ q = Q / m = {DFF(l[0])} / {DFF(l[2])} = {a} Дж/кг * °C'
	if l[2] == '-':
		a = DFF(DFF(l[0]) / DFF(l[1]))
		return f'Ваш ответ m = Q / q = {DFF(l[0])} / {DFF(l[1])} = {a} кг'
	return 'Что-то введено некорректно'

def URV(message):
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

def geo(message, local_data):
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
			markup = types.ReplyKeyboardMarkup()    
			SubjectButton1 = types.KeyboardButton('/clear')
			markup.add(SubjectButton1)
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, видимо в нашей базе ещё нет этой страны. Мы получили данные от вашего запроса и страна будет добавлена в ближайшее время. Нажмите /clear для выхода или наберите другое название', reply_markup=markup)
			print(message.text)

def pss(message):
	num10 = 0
	l = message.text.split()
	if len(l) == 3:
		if int(l[1]) > 0 and int(l[2]) > 0 and int(l[1]) < 11 and int(l[2]) < 11:
			num = int(l[0])
			o1 = int(l[1])
			o2 = int(l[2])
			res = 0
			strnum = str(num)[::-1]
			s = ''
			for i in range(len(strnum)):
				num10 += int(strnum[i]) * (o1 ** i)
			while num10!=0:
				s += str(num10 % o2)
				num10 //= o2
			bot.send_message(message.from_user.id, s[::-1])
			
			


@bot.message_handler(content_types=['text'])			
def main(message):
	list_conv = ['скорость', 'длина', 'время', 'данные', 'масса', 'объем', 'температура', 'энергия', 'площадь', 'мощность', 'давление', 'угол']
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
	elif len(local_data) == 1 and local_data[0] == 'разное': 													#ВЕТКА СПРАВОЧНЫЕ МАТЕРИАЛЫ
		local_data.append(message.text.lower())
		markup = types.ReplyKeyboardRemove(selective=False)
		if local_data[1] == 'география':
			bot.send_message(message.from_user.id, 'Введи название страны, что бы получить основную информацию о ней:', reply_markup=markup)
		elif local_data[1] == 'математика':
			markup = types.ReplyKeyboardMarkup()
			physchapter1 = types.KeyboardButton('Тригонометрические функции')
			markup.add(physchapter1)
			bot.send_message(message.from_user.id, 'Выбери тему:', reply_markup=markup)
		elif local_data[1] == 'перевод систем счисления':
			bot.send_message(message.from_user.id, 'Введите данные в формате "*число для перевода* *система счисления вашего числа* *нужная система счисления*" (Основание системы счисления не может быть отрицательным и больше 10, в дальнейшем будет 16-ричная система.)', reply_markup=markup)
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, для помощи напиши команду  /help', reply_markup=markup)
	elif len(local_data) == 2 and local_data[0] == 'разное' and message.text.lower() == 'тригонометрические функции':
		markup = types.ReplyKeyboardMarkup()
		physchapter1 = types.KeyboardButton('Таблица')
		markup.add(physchapter1)
		bot.send_message(message.from_user.id, 'Введите задание в формате (название тригонометрической функции)градусы. Если угол дан в радианах, добавь r  в конец без пробелов. Например ctg45. (таблица - для получения таблицчных значений)', reply_markup=markup)
		local_data.append(message.text.lower())
	elif len(local_data) == 3 and local_data[0] == 'разное' and local_data[2] == 'тригонометрические функции':
		if message.text.lower() == 'таблица':
			bot.send_photo(message.from_user.id, photo='https://ru-static.z-dn.net/files/d3e/e92377a60bc0dea6c8c17a21c126898f.jpg')
			local_data = []
		elif Trygonometry(message.text.lower()) != None:
			bot.send_message(message.from_user.id, Trygonometry(message.text.lower()))
			local_data = []
		else:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 1 and local_data[0] == 'конвертер величин': 													#ВЕТКА СПРАВОЧНЫЕ МАТЕРИАЛЫ
		local_data.append(message.text.lower())
		markup = types.ReplyKeyboardRemove(selective=False)
		if local_data[1] in list_conv:
			bot.send_message(message.from_user.id, 'Введи числовое значение величины', reply_markup=markup)
		else:
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, для помощи напиши команду  /help', reply_markup=markup)
	elif len(local_data) == 2 and local_data[0] == 'разное' and local_data[1] == 'география':						#ВЫВОДИТ СПРАВКУ О СТРАНАХ			markup = types.ReplyKeyboardRemove(selective=False)
		geo(message, local_data)
	elif len(local_data) == 2 and local_data[0] == 'разное' and local_data[1] == 'перевод систем счисления':
		pss(message)
	elif len(local_data) == 1 and local_data[0] == 'решение задач':														#ВЕТКА РЕШЕНИЕ ЗАДАЧ
		if message.text.lower() == 'физика':
			markup = types.ReplyKeyboardMarkup()
			physchapter1 = types.KeyboardButton('Термодинамика')
			physchapter2 = types.KeyboardButton('Термодинамика сгорания')
			markup.add(physchapter1, physchapter2)
			bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
			local_data.append(message.text.lower())
		elif message.text.lower() == 'математика':
			markup = types.ReplyKeyboardMarkup()
			physchapter1 = types.KeyboardButton('Алгебра')
			physchapter2 = types.KeyboardButton('Теорема Пифагора')
			markup.add(physchapter1, physchapter2)
			bot.send_message(message.from_user.id, "Выберите раздел", reply_markup=markup)
			local_data.append(message.text.lower())
		else:
			markup = types.ReplyKeyboardMarkup()    
			SubjectButton1 = types.KeyboardButton('Физика') 
			SubjectButton2 = types.KeyboardButton('Математика') 
			markup.add(SubjectButton1, SubjectButton2)
			bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю, выбери нужный тебе предмет:', reply_markup=markup)
	elif len(local_data) == 2 and message.text.lower() == 'теорема пифагора':
		bot.send_message(message.from_user.id, "Введите катеты/гипотенузу и катет в формате a b c, известные величины - числами, неизвестную - '-'")
		local_data.append(message.text.lower())
	elif len(local_data) == 3 and local_data[2] == 'теорема пифагора' and pifagor(message.text.lower() != None):
		bot.send_message(message.from_user.id, pifagor(message.text.lower()))
		user_data[message.from_user.id] = [] 
	elif len(local_data) == 3 and local_data[2] == 'теорема пифагора' and pifagor(message.text.lower() == None):
		bot.send_message(message.from_user.id, 'Прости, я тебя не понимаю')
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
		URV(message)
	elif len(local_data) == 3 and message.text.lower() == 'q':	
		markup = types.ReplyKeyboardRemove(selective=False)																	
		bot.send_message(message.from_user.id, "Введите удельную теплоёмкость (Дж/кг * °C)", reply_markup=markup)
		local_data.append(message.text.lower())
	elif len(local_data) == 2 and message.text.lower() == 'термодинамика сгорания':
		markup = types.ReplyKeyboardRemove(selective=False)																	
		bot.send_message(message.from_user.id, "Введите по порядку через пробел Q, q, m. Для указания неизвестного используйте -", reply_markup=markup)
		local_data.append('сгорание')
	elif len(local_data) == 3 and local_data[2] == 'сгорание':
		bot.send_message(message.from_user.id, burn(message.text.lower()))
	elif len(local_data) == 4 and local_data[3] == 'q':
		markup = types.ReplyKeyboardRemove(selective=False)
		v1 = DFF(message.text.lower())
		if v1 != None:
			if v1 >= 0:
				local_data.append(v1)
				bot.send_message(message.from_user.id, "Введите начальную температуру (°C)", reply_markup=markup)
			else:
				bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
		elif v1 == None:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 5 and local_data[3] == 'q':
		v1 = DFF(message.text.lower())
		if v1 != None:
			local_data.append(v1)
			bot.send_message(message.from_user.id, "Введите конечную  температуру (°C)")
		elif v1 == None:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 6 and local_data[3] == 'q':
		v1 = DFF(message.text.lower())
		if v1 != None:
				local_data.append(v1)
				bot.send_message(message.from_user.id, "Введите массу (кг)")
		elif v1 == None:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 7 and local_data[3] == 'q':
		v1 = DFF(message.text.lower())
		if v1 != None and v1 > 0:
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
		else:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')	
	elif len(local_data) == 3 and message.text.lower() == 'c':	
		markup = types.ReplyKeyboardRemove(selective=False)
		bot.send_message(message.from_user.id, "Введите количество теплоты (Дж)", reply_markup=markup)
		local_data.append(message.text.lower())
	elif len(local_data) == 4 and local_data[3] == 'c':
		v1 = DFF(message.text.lower())
		if v1 != None:
			local_data.append(v1)
			bot.send_message(message.from_user.id, "Введите начальную температуру (°C)")
		elif v1 == None:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 5 and local_data[3] == 'c':
		v1 = DFF(message.text.lower())
		if v1 != None:
			local_data.append(v1)
			bot.send_message(message.from_user.id, "Введите конечную  температуру (°C)")
		elif v1 == None:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 6 and local_data[3] == 'c':
		v1 = DFF(message.text.lower())
		if v1 != None:
			local_data.append(v1)
			bot.send_message(message.from_user.id, "Введите массу (кг)")
		elif v1 == None:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
	elif len(local_data) == 7 and local_data[3] == 'c':
		v1 = DFF(message.text.lower())
		if v1 != None:
			if v1 >= 0:
				local_data.append(v1)
				bot.send_message(message.from_user.id, f'''Q = cm(t₂ - t₁)
c = Q / (m * (t₂ - t₁))
c = {int(local_data[4])} / ({int(local_data[7])} * ({int(local_data[6])} - {int(local_data[5])}))
Ответом на эту задачу является: {round(local_data[4]  / (local_data[6] - local_data[5]) * local_data[7])} (Дж/кг * °C).''')
				user_data[message.from_user.id] = []
			else:
				bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
		else:
			bot.send_message(message.from_user.id, 'Что-то введено некорректно.')
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
	elif len(local_data) == 2 and local_data[1] == 'время':
		local_data.append(float(message.text))
		markup = types.ReplyKeyboardMarkup()
		Speed1 = types.KeyboardButton('с')
		Speed2 = types.KeyboardButton('мин')
		Speed3 = types.KeyboardButton('часы')
		markup.add(Speed1, Speed2, Speed3)
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'с':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''с - {speed}
мин - {speed / 60}
часы - {speed / 3600}
''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 3 and message.text.lower() == 'мин':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''с - {speed * 60}
мин - {speed}
часы - {speed / 60}
''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 3 and message.text.lower() == 'часы':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''с - {speed * 3600}
мин - {speed * 60}
часы - {speed}
''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 2 and local_data[1] == 'длина':
		local_data.append(float(message.text))
		markup = types.ReplyKeyboardMarkup()
		Speed1 = types.KeyboardButton('м')
		Speed2 = types.KeyboardButton('км')
		Speed3 = types.KeyboardButton('мили')
		markup.add(Speed1, Speed2, Speed3)
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'м':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''м - {speed}
		км - {speed / 1000}
		мили - {speed / 1610}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'км':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''м - {speed * 1000}
		км - {speed}
		мили - {speed / 1.61}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'мили':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f''' м - {speed * 1610}
		км - {speed * 1.61}
		мили - {speed}
		''')
		user_data[message.from_user.id] = []
	elif len(local_data) == 2 and local_data[1] == 'данные':
		local_data.append(float(message.text))
		markup = types.ReplyKeyboardMarkup()
		Speed1 = types.KeyboardButton('биты')
		Speed2 = types.KeyboardButton('байты')
		Speed3 = types.KeyboardButton('Кб')
		Speed4 = types.KeyboardButton('Мб')
		Speed5 = types.KeyboardButton('Гб')
		markup.add(Speed1, Speed2, Speed3, Speed4, Speed5)
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'биты':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''биты - {speed}
		байты - {speed / 8}
		Кб - {speed / 8 / 1024}
		Мб - {speed / 8 / 1024 / 1024}
		гб - {speed / 8 /1024 / 1024 / 1024}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'байты':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''биты - {speed * 8}
		байты - {speed}
		Кб - {speed / 1024}
		Мб - {speed / 1024 / 1024}
		гб - {speed / 1024 / 1024 / 1024}
		''')
		user_data[message.from_user.id] = []  	
	elif len(local_data) == 3 and message.text.lower() == 'кб':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''биты - {speed * 8 * 1024}
		байты - {speed * 1024}
		Кб - {speed}
		Мб - {speed / 1024}
		гб - {speed / 1024 / 1024}
		''')
		user_data[message.from_user.id] = []  	
	elif len(local_data) == 3 and message.text.lower() == 'мб':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''биты - {speed * 8 * 1024 * 1024}
		байты - {speed * 1024 * 1024}
		Кб - {speed * 1024}
		Мб - {speed}
		гб - {speed / 1024}
		''')
		user_data[message.from_user.id] = []  	
	elif len(local_data) == 3 and message.text.lower() == 'гб':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''биты - {speed * 1024 * 1024 * 1024 * 8}
		байты - {speed * 1024 * 1024 * 1024}
		Кб - {speed * 1024 * 1024}
		Мб - {speed * 1024}
		гб - {speed}
		''')
	elif len(local_data) == 2 and local_data[1] == 'масса':
		local_data.append(float(message.text))
		markup = types.ReplyKeyboardMarkup()
		Speed1 = types.KeyboardButton('мг')
		Speed2 = types.KeyboardButton('г')
		Speed3 = types.KeyboardButton('кг')
		Speed4 = types.KeyboardButton('фунт')
		markup.add(Speed1, Speed2, Speed3, Speed4)
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'мг':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''мг - {speed}
г - {speed / 1000}
кг - {speed / 1000000}
фунт - {speed / 453592,37}
''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 3 and message.text.lower() == 'г':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''мг - {speed * 1000}
г - {speed}
кг - {speed/1000}
фунт - {speed * 453,59237}
''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 3 and message.text.lower() == 'кг':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''мг - {speed * 1000000}
г - {speed * 1000}
кг - {speed}
фунт - {speed / 0.4536}
''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 3 and message.text.lower() == 'фунт':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''мг - {speed * 453600}
г - {speed * 453.6}
кг - {speed * 0,4536}
фунт - {speed}
''')
		user_data[message.from_user.id] = []	
	elif len(local_data) == 2 and local_data[1] == 'температура':
		local_data.append(float(message.text))
		markup = types.ReplyKeyboardMarkup()
		Speed1 = types.KeyboardButton('°C')
		Speed2 = types.KeyboardButton('K')
		Speed3 = types.KeyboardButton('°F')
		markup.add(Speed1, Speed2, Speed3)
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == '°c':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''°C - {speed}
		K - {speed + 273}
		°F - {speed * 1.8 + 32}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'k':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''°C - {speed - 273}
		K - {speed}
		°F - {speed * 1.8 - 459}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == '°f':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''°C - {(speed - 32) / 1.8}
		K - {(speed + 459) / 1.8}
		°F - {speed}
		''')
		user_data[message.from_user.id] = []
	elif len(local_data) == 2 and local_data[1] == 'площадь':
		local_data.append(float(message.text))
		markup = types.ReplyKeyboardMarkup()
		Speed1 = types.KeyboardButton('см²')
		Speed2 = types.KeyboardButton('м²')
		Speed3 = types.KeyboardButton('км²')
		markup.add(Speed1, Speed2, Speed3)
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'см²':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''см² - {speed}
		м² - {speed / 10000}
		км² - {speed / 100000000}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'м²':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''см²- {speed * 10000}
		м² - {speed}
		км² - {speed / 10000}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'км²':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''см² - {speed * 100000000}
		м² - {speed * 10000}
		км² - {speed}
		''')
		user_data[message.from_user.id] = []
	elif len(local_data) == 2 and local_data[1] == 'объем':
		local_data.append(float(message.text))
		markup = types.ReplyKeyboardMarkup()
		Speed1 = types.KeyboardButton('см³')
		Speed2 = types.KeyboardButton('м³')
		Speed3 = types.KeyboardButton('км³')
		markup.add(Speed1, Speed2, Speed3)
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'см³':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''см³ - {speed}
		м³ - {speed / 1000000}
		км³ - {speed / 1000000000000}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'м³':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''см³- {speed * 1000000}
		м³ - {speed}
		км³ - {speed / 1000000}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'км³':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''см³ - {speed * 1000000000000}
		м³ - {speed * 1000000}
		км³ - {speed}
		''')
		user_data[message.from_user.id] = []
	elif len(local_data) == 2 and local_data[1] == 'энергия':
		local_data.append(float(message.text))
		markup = types.ReplyKeyboardMarkup()
		Speed1 = types.KeyboardButton('Дж')
		Speed2 = types.KeyboardButton('кДж')
		Speed3 = types.KeyboardButton('калории')
		markup.add(Speed1, Speed2, Speed3)
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'дж':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''дж - {speed}
		кДж - {speed / 1000}
		калории - {speed / 4.18}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'кдж':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''дж - {speed * 1000}
		кДж - {speed}
		калории - {speed / 4.18 * 1000}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'калории':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''дж - {speed * 4.18}
		кДж - {speed * 4.18 / 1000}
		калории - {speed}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 2 and local_data[1] == 'мощность':
		local_data.append(float(message.text))
		markup = types.ReplyKeyboardMarkup()
		Speed1 = types.KeyboardButton('Вт')
		Speed2 = types.KeyboardButton('кВт')
		markup.add(Speed1, Speed2)
		bot.send_message(message.from_user.id, 'Выберите вашу величину', reply_markup=markup)
	elif len(local_data) == 3 and message.text.lower() == 'вт':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''Вт - {speed}
		кВт - {speed / 1000}
		''')
		user_data[message.from_user.id] = []  
	elif len(local_data) == 3 and message.text.lower() == 'квт':
		speed = round(float(local_data[2]), 3)
		bot.send_message(message.from_user.id, f'''Вт - {speed * 1000}
		кВт - {speed}
		''')
		user_data[message.from_user.id] = [] 
	print(user_data)      
#	print(ideas_data)                                                                                                                             
bot.infinity_polling(timeout=1080)