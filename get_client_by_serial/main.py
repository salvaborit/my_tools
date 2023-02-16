#!/usr/bin/python3

import csv


def csv_to_dicts(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


data = csv_to_dicts('control.csv')

while True:
    input_serial = input('Ingresar serial: ')
    if input_serial == 'quit' or input_serial == 'exit':
        exit()

    errores_scanner = {
        '1': '!',
        '2': '@',
        '3': '#',
        '4': '$',
        '5': '%',
        '6': '^',
        '7': '&',
        '8': '*',
        '9': '(',
        '0': ')',
    }

    for key, val in errores_scanner.items():
        if val in input_serial:
            input_serial = input_serial.replace(val, key)

    for item in data:
        if item['serie'].upper() == input_serial.upper():
            print(item['cliente'])
            break
    else:
        print('NO ENCONTRADA')
