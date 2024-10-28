#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Список работников.
    workers = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            name = input("Фамилия и инициалы? ")
            numb = input("Телефон? ")
            date = list(map(int, (input("Дата рождения? ")).split()))

            # Создать словарь.
            worker = {
                'name': name,
                'numb': numb,
                'date': date,
            }

            # Добавить словарь в список.
            workers.append(worker)
            # Отсортировать список в случае необходимости.
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == 'month':
            key_count1 = 0
            key_count2 = 0
            # Запросить искомый месяц.
            key_month = int(input("Месяц? "))

            # Найти соответствующих сотрудников.
            for key_count1, item in enumerate(workers):
                if key_month == workers[key_count1]["date"][1]:
                    print(workers[key_count1])
                    key_count2 += 1
            if key_count2 == 0:
                print('Сотрудников с указанными параметрами не найдено')

    # Вывести результат.
    print("Отсортированный список:")
    for item in workers:
        print(item)
