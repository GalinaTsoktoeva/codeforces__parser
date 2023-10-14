import os
import django
import random
import time

from django.conf import settings
from django.core.management import BaseCommand
from telebot import TeleBot

from task.models import Task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django.settings')
django.setup()

bot = TeleBot(settings.TELEGRAM_API, threaded=False)


class Command(BaseCommand):

    help = 'Just a command for lauching a Telegram bot'

    def handle(self, *args, **kwargs):
        # Сохранение обработчиков
        bot.enable_save_next_step_handlers(delay=2)
        # Загрузка обработчиков
        bot.load_next_step_handlers()

        @bot.message_handler(commands=['start'])
        def start(message):
            mess = (f'Привет, <b>{message.from_user.first_name}</b> <u>{message.from_user.last_name}</u>! \n/'
                    f'Этот супер бот поможет выбрать тебе задачи с сайта CODEFORCES\n/'
                    f'Введите сложность задачи и тему\n'
                    f'Например: 1000 math'
                    )
            bot.send_message(message.chat.id, mess, parse_mode='html')

        @bot.message_handler()
        def get_user_text(message):
            task_list = []
            result = []

            text = message.text.split()

            if text:
                for item_filter in text:
                    if item_filter.isdigit():
                        complex = list(Task.objects.filter(complexity=item_filter))
                        task_list.extend(complex)
                    else:
                        tag = list(Task.objects.filter(tags__icontains=item_filter))
                        task_list.extend(tag)

            if task_list:
                for item_task in task_list:
                    result.append(item_task.name + " " + item_task.numbers)

            if not result:
                answer = "Нет задач с необходимой темой и сложностью"
            else:
                finish = random.sample(result, 10)
                answer = ", ".join(finish)
            bot.send_message(message.chat.id, answer)

        # Бесконечный цикл бота
        while True:
            try:
                bot.polling(none_stop=True)
            except Exception():
                print('upalo')
                time.sleep(5)
