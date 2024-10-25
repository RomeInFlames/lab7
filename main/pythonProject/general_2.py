#!/usr/bin/env python3
# -*- coding: utf-8 -*-

riddle = {
    '1': 'Лепестки ворожат —',
    '2': 'Мельтешит и мерцает храм',
    '3': 'Сквозь ветви сакуры.',
    }

n = riddle.items()
swapped = dict(map(reversed, n))

print(swapped)


