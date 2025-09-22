import os
import sys
import django
from dotenv import load_dotenv

# Добавляем корневую папку проекта в путь
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import telebot
from telebot import types
from sports.models import Sport, Coach, Place, District, SportPlace, CoachSportPlace


load_dotenv()
TG_BOT = os.getenv('TELEGRAM_BOT')


class TelegramBot:
    def __init__(self, token: str):
        self.bot = telebot.TeleBot(token)
        self._register_handlers()


    # методы обработки команд
    def start_handler(self, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вид спорта')
        btn2 = types.KeyboardButton('Место проведения')
        btn3 = types.KeyboardButton('Район')
        btn4 = types.KeyboardButton('Тренера')
        markup.row(btn1, btn2, btn3, btn4)


        self.bot.send_message(message.chat.id, f"Привет! \n{message.from_user.first_name}, ты находишься в информационном портале 'Спортивные секции города Перми'. Тут можно найти где и в каком месте есть спортивные секции для детей. Секции есть как платные так и бесплатные", reply_markup=markup)

        self.bot.register_next_step_handler(message, self.on_click)

    def info_handler(self, message):
        self.bot.send_message(message.chat.id, "Доступные команды: /start, /hello, /help")

    def user_text_handler(self, message):
        msg_list = ['start', 'main', 'hello', 'help']
        if message.text.lower() == 'id':
            self.bot.reply_to(message, f'Ваш ID: {message.from_user.id}')
        elif message.text.lower() not in msg_list:
            self.info_handler(message)


    # Обработка выбора кнопок
    def on_click(self, message):
        if message.text == 'Вид спорта':
            self.bot.send_message(message.chat.id, 'Тут будут виды спорта из БД')
        elif message.text == 'Место проведения':
            self.bot.send_message(message.chat.id, 'Тут будут места проведения из БД')
        elif message.text == 'Район':
            self.bot.send_message(message.chat.id, 'Тут будут районы из БД')
        elif message.text == 'Тренера':
            self.bot.send_message(message.chat.id, 'Тут будут тренеры из БД')

    # регистрация обработчика
    def _register_handlers(self):
        self.bot.register_message_handler(self.start_handler, commands=['start', 'main', 'hello'])
        self.bot.register_message_handler(self.info_handler, commands=['help'])
        self.bot.register_message_handler(self.user_text_handler)


    # запуск бота
    def run_bot(self):
        self.bot.infinity_polling()


if __name__ == '__main__':
    bot = TelegramBot(TG_BOT)
    bot.run_bot()