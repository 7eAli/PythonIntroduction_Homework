# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot
import random

bot = telebot.TeleBot("6098227235:AAGK3FZwifIBtN02O3h9r9yV-rmVY-UYxK0")

@bot.message_handler(commands=['обращение'])
def request_handling(message):
    print(message)
    bot.send_message(message.from_user.id, 'Запишите свое обращение')
    @bot.message_handler(content_types=['text'])
    def requests(message):
        data = open('requests_log.txt', mode='a', encoding='utf-8')
        data.writelines(f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n')
        data.close()


bot.polling()