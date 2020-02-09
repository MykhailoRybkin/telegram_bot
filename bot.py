import telebot
import config
from telebot import types


import random

TOKEN ='935757526:AAGFm0C8tqLZo3LMPBhcW43BxqWm_YkOGJI'

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):


	
		stic = open('C:/Users/48796/Desktop/bot/stick1.webp', 'rb')
		bot.send_sticker(message.chat.id, stic)

		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Łukasz")
		item2 = types.KeyboardButton("Jurets")
		item3 = types.KeyboardButton("Скок см хуй Юрца?")
		item4 = types.KeyboardButton("Я - Мішаня/Міхалич")
		item5 = types.KeyboardButton("Кнопка для девок")
		item6 = types.KeyboardButton("Играть в игру")

	

		markup.add(item1, item2, item3, item4, item5, item6)

		bot.send_message(message.chat.id, "Добро пожаловать", parse_mode='html', reply_markup=markup)

		




@bot.message_handler(content_types=['text'])
def lalala(message):


	sti = open('C:/Users/48796/Desktop/bot/sticker.webp', 'rb')
	image = open('C:/Users/48796/Documents/photo_2019-12-01_23-59-56.jpg', 'rb')
	
	if message.text == 'Jurets':
    		bot.send_sticker(message.chat.id, sti)
	elif message.text == 'Łukasz':
			bot.send_message(message.chat.id, "Маєш 5 мінут")
	elif message.text == 'Скок см хуй Юрца?':
			bot.send_message(message.chat.id, str(random.randint(0,25)))
	elif message.text == 'Я - Мішаня/Міхалич':
			mishania = types.InlineKeyboardMarkup(row_width=2)
			key_mish = types.InlineKeyboardButton(text='Мішаня', callback_data='good')
			key_mich = types.InlineKeyboardButton(text='Міхалич', callback_data='perfect')
			mishania.add(key_mish)
			mishania.add(key_mich)
			bot.send_message(message.chat.id, "Дак ти хто конкретно?", reply_markup=mishania)
	elif message.text == 'Юрец':
			bot.send_message(message.chat.id, 'Соси хуец ахахахах')
	#elif message.text == 'Міхалич' or 'Мішаня':
			#bot.send_message(message.chat.id, 'Пішов нахуй')
	elif message.text == 'Хто миє кухню?':
			kto = types.InlineKeyboardMarkup(row_width=2)
			key_yes = types.InlineKeyboardButton(text='Тянуть карту', callback_data='yes')
			kto.add(key_yes)	 
			bot.send_message(message.chat.id, "Держи", reply_markup=kto)
	elif message.text == 'Кнопка для девок':
			devki = types.InlineKeyboardMarkup(row_width=2)
			key_yes = types.InlineKeyboardButton(text='Тянуть карту', callback_data='no')
			devki.add(key_yes)	 
			bot.send_message(message.chat.id, "Держи", reply_markup=devki)
	elif message.text == 'Покажи лучших в мире':
			bot.send_photo(message.chat.id, image)
	
	else:
			bot.send_message(message.chat.id, 'Сарян, больше я нихуя пока не знаю, мой разработчик - даун')



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'yes':
				li=[]
				koloda=dict(Двойка=2,Тройка=3,Четверка=4,Пятерка=5,Шестерка=6,Семерка=7,Восьмерка=8,Девятка=9,Десятка=10,Валет=11,Дама=12,Король=13,Туз=14,Джокер=15)
				a=random.choice(list(koloda.items()))
				li.append(a[1])
				bot.send_message(call.message.chat.id, "Віталі випало: " + ' ' + str(a[0]))
				b=random.choice(list(koloda.items()))
				li.append(b[1])
				bot.send_message(call.message.chat.id,'Юрцу випало:' + ' ' + str(b[0]))
				c=random.choice(list(koloda.items()))
				li.append(c[1])
				bot.send_message(call.message.chat.id,'Мішані випало:' + ' ' + str(c[0]))
				d=random.choice(list(koloda.items()))
				li.append(d[1])
				bot.send_message(call.message.chat.id,'Міхаличу випало:'+ ' ' + str(d[0]))
				min_wart = min(li)
				if min_wart == li[0]:
					bot.send_message(call.message.chat.id,'Проєбав Віталя')
				if min_wart == li[1]:
					bot.send_message(call.message.chat.id,'Проєбав Юрец, ахахахаха лошара')
				if min_wart == li[2]:
					bot.send_message(call.message.chat.id,'Проєбав Мішаня')
				if min_wart == li[3]:
					bot.send_message(call.message.chat.id,'Проєбав Міхалич')
			if call.data == 'good':
				bot.send_message(call.message.chat.id,'Шо там Настя?')
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Мені на тебе похуй",
                reply_markup=None)
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="ПОХУЙ")
			if call.data == 'perfect':
				bot.send_message(call.message.chat.id,'Hala Madrid!')
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Мені на тебе похуй",
                reply_markup=None)
			if call.data == 'no':
				li=[]
				koloda=dict(Двойка=2,Тройка=3,Четверка=4,Пятерка=5,Шестерка=6,Семерка=7,Восьмерка=8,Девятка=9,Десятка=10,Валет=11,Дама=12,Король=13,Туз=14,Джокер=15)
				a=random.choice(list(koloda.items()))
				li.append(a[1])
				bot.send_message(call.message.chat.id, "Лізі випало: " + ' ' + str(a[0]))
				b=random.choice(list(koloda.items()))
				li.append(b[1])
				bot.send_message(call.message.chat.id,'Лері випало:' + ' ' + str(b[0]))
				c=random.choice(list(koloda.items()))
				li.append(c[1])
				bot.send_message(call.message.chat.id,'Насті випало:' + ' ' + str(c[0]))
				
				min_wart = min(li)
				if min_wart == li[0]:
					bot.send_message(call.message.chat.id,'Проєбала Ліза')
				if min_wart == li[1]:
					bot.send_message(call.message.chat.id,'Проєбала Лера')
				if min_wart == li[2]:
					bot.send_message(call.message.chat.id,'Проєбала Настя')

				
				
		

	except Exception as e:
		print(repr(e))

	

bot.polling(none_stop = True)