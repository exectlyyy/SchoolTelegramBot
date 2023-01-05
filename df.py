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