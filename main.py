#Код до переноса на https://www.pythonanywhere.com/

import random

HELP = '''
help = вывести список доступных команд
add = добавить задачу в список
show = напечатать все добавленные задачи
exit = выход из программы
random = добавлять случайную задачу на дату Сегодня'''

def add_todo(date_task, task):
    if date_task in tasks:
        # дата есть в словаре
        # добавляем в список задачу
        tasks[date_task].append(task)
    else:
        # даты нет в словаре, создаем запись с ключом
        tasks[date_task] = []
        tasks[date_task].append(task)
    print('Задача', task, 'добавлена на дату', date_task)

random_tasks = ['выпить кофе', 'позаниматься программированием', 'почитать книгу "Простой python"', 'хорошенько отдохнуть', 'пойти поспать']
tasks = {

}

run = True

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        date = input('Введите дату для отображения списка задач: ')
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print('Нет задач на введенную дату')
    elif command == 'add':
        date_task = input('Введите дату задачи: ')
        task = input('Введите название задачи: ')
        add_todo(date_task, task)
    elif command == 'random':
        task = random.choice(random_tasks)
        add_todo("сегодня", task)
    elif command == 'exit':
        print('Спасибо за использование! До следующей встречи!')
        break
    else:
        print('Неизвестная команда')
