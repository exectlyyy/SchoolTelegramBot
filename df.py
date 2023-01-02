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