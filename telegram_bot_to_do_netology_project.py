# телеграм-бот размешён через www.pythonanywhere.com
# бот принимает от пользователя команду на добавление задачи на определённую дату. По команде выводит перечень всех имеющихся задач. 

import telebot
import random

token = '2010273573:AAF-chsJjiWh6nlMlk1gR0cYNKHDe7104as'
bot = telebot.TeleBot(token)
HELP = '''
/help = вывести список доступных команд
/add = добавить задачу в список
/show = напечатать все добавленные задачи
/random = добавить случайную задачу на дату Сегодня'''
random_tasks = ['выпить кофе', 'позаниматься программированием', 'почитать книгу "Простой python"', 'хорошенько отдохнуть', 'пойти поспать']

tasks = {}

def add_todo(date_task, task):
    if date_task in tasks:
        # дата есть в словаре
        # добавляем в список задачу
        tasks[date_task].append(task)
    else:
        # даты нет в словаре, создаем запись с ключом
        tasks[date_task] = []
        tasks[date_task].append(task)



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    text = 'Задача ' + task + ' добавлена на дату: ' + date
    add_todo(date, task)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['random'])
def random_add(message):
    date = 'сегодня'
    task = random.choice(random_tasks)
    text = 'Задача ' + task + ' добавлена на дату: ' + date
    add_todo(date, task)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show', 'print'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ''
    if date in tasks:
        text = date.upper() + '\n'
        for task in tasks[date]:
            text = text + '[] ' + task + '\n'
    else:
        text = 'Задач на запрашиваемую дату нет'
    bot.send_message(message.chat.id, text)

bot.polling(none_stop = True)
