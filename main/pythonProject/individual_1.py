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
            key_count = 0
            key_month = int(input("Месяц? "))
            while len(workers) >= key_count and key_month == workers[key_count]["date"][1]:
                print(worker)
                key_count += 1

    print(workers)
                    
    print(workers)
