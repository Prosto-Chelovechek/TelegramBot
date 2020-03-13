import telebot
bot = telebot.TeleBot("мой токен")

import pyowm
owm = pyowm.OWM('мой токен', language = "ru")

@bot.message_handler(commands = ['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, введи свой город\n(потом его нельзя будет поменять)")

@bot.message_handler(content_types = ['text'])
def echo_message(message):
	global place
	place = message.text
	observation = owm.weather_at_place(place)
	w = observation.get_weather()
	global temp
	temp = str(w.get_temperature('celsius')["temp"])
	global stat
	stat = w.get_detailed_status
	bot.send_message(message.chat.id, "Спасибо, ваш город это - " + place + "\nКогда надо будет узнать погоду напиши \"погода\"")

while True:
	@bot.message_handler(content_types = ['text'])
	def handle_message(message):
		start = message.text
		if start == "погода" or "Погода":
			bot.send_message(message.chat.id, "Сейчас примерно " + temp + " и " + stat)
		else:
			bot.send_message(message.chat.id, "Вы ошиблись")

bot.polling( none_stop = True )
