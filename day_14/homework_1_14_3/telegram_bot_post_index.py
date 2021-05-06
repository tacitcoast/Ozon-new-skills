# Используя библиотеку pyTelegramBotAPI напишите телеграм-бота, который получает от пользователя команду в формате /index <почтовый_индекс>,
# затем обращается к бесплатному API https://api.zippopotam.us/ru/ и возвращает пользователю сообщение в формате ИНДЕКС, СТРАНА, ГОРОД
# Например, /index 101000 должен вернуть 101000: Russia Москва.

import re

import requests
import telebot

# Сохраняем наш токен
token = 'token'

# Создаем бот
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['index'])
def get_index_info(message):
    if re.match('^/index ([0-9]{6})$', message.text):
        # Берем значение только число
        post_index = message.text.split()[1]
        # Делаем запрос к api с индектос
        result = requests.get('https://api.zippopotam.us/ru/' + post_index)
        # Переводим json в словарь
        json_response = result.json()
        print(json_response)

        # Создаем пустую переменную для страны, на случай, если не будет данных
        country = ''
        if 'country' in json_response:
            country = json_response['country']

        # Создаем пустую переменную для города, на случай, если не будет данных
        city = ''
        if 'places' in json_response:
            # Создаем цикл для массива, поскольку не известно количество элементов
            for place in json_response['places']:
                city = place['state']
                # Выходим на первом же совпадении
                break

        # Выводим ответ с необходимыми значениями
        bot.reply_to(message, '{}: {} {}'.format(post_index, country, city))


# Мониторим телеграм канал с заданным токеном
bot.infinity_polling()