#!/usr/bin/env python3
# -*- coding: utf-8 -*-

school = {'a1': '30', 'b1': '32', 'c1': '29', 'd1': '31'}
print("До изменений:", school)

school['a1'] = 29
school.setdefault("e1", '14')
school.pop('d1')

print("После изменений:", school)