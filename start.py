__author__ = 'Nick Terskikh'
# -*- coding: utf-8 -*-
# 06.05.2018

import configparser
import os

# Проверка наличия файла со значениями values.ini в текущем каталоге
if not os.path.exists("values.ini"):
    print('Файл переменных values.ini в текущем каталоге не найден! Программа завершена.')
    print('Файл values.ini должен содержать следующее: ')
    print('\nПеременные(числа):')
    print('# grafik - оплата за смену на графиках')
    print('# support - оплата за смену на саппорте')
    print('# podmena - оплата за смену на подмене')
    print('# cp - оплата за одну перевыпущенную ЦП')
    print('# free - надбавка в выходные за работу')
    print('# stavka - процент надбавки за переводы в платёжных системах')
    print('# shtraf - штрафные санкции')
    print('\nПример содержимого файла values.ini:')    
    print('\n[value]')
    print('grafik  = 2200')
    print('support = 2000')
    print('podmena = 1800')
    print('cp = 100')
    print('free = 200')
    print('stavka = 1.03')
    print('shtraf = 200')
    input('\nДля завершения работы программы нажмите Enter...')
    raise SystemExit(1)  # завершаем работу программы

# Чтение значений переменных из файла values.ini, который должен быть расположен в этом же каталоге и присваивание им
config = configparser.ConfigParser()
config.read("values.ini")
grafik = float(config.get("value", "grafik"))
support = float(config.get("value", "support"))
podmena = float(config.get("value", "podmena"))
cp = float(config.get("value", "cp"))
free = float(config.get("value", "free"))
stavka = float(config.get("value", "stavka"))
shtraf = float(config.get("value", "shtraf"))

# Запрос исходных данных у пользователя
print('*** Вас приветствует программа подсчёта зарплаты саппорта ***\n')
grafik_number = float(input('Введите кол-во смен на графиках(введите число): '))
grafik_free = float(input('Сколько графиков совпало на выходные(введите число): '))
support_number = float(input('Введите кол-во смен на саппорте(введите число): '))
podmena_number = float(input('Введите кол-во смен на подмене(введите число): '))
cp_number = float(input('Сколько было перевыпущено ЦП(введите число): '))
other = float(input('Прочие выплаты или Бонус(введите число): '))
shtraf = float(input('Штраф(введите число): '))

# Логика программы
# Подсчёт промежуточных результатов зарплаты
grafik_free_all = grafik_free * free
cp_number_all = cp_number * cp
grafik_all = grafik_number * grafik
support_all = support_number * support
podmena_all = podmena_number * podmena

# Подсчет и вывод зарплаты
salary = (grafik_free_all + cp_number_all + grafik_all + support_all + podmena_all + other) - shtraf
print('\n(', grafik_free_all, '+', cp_number_all, '+', grafik_all, '+', support_all, '+', podmena_all, '+', other, ')', '-', shtraf, '=', salary)
print('\nВаша зарплата: ')
print(salary, 'руб.')
print('\nВаша конечная зарплата с процентной ставкой составит: ')
print(salary * stavka, 'руб.')
print('\n***Конец***')
input('\nДля завершения работы программы нажмите Enter...')