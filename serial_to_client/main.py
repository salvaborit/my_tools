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

    scanner_errors = {
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

    for key, val in scanner_errors.items():
        if val in input_serial:
            input_serial = input_serial.replace(val, key)

    for item in data:
        if item['serial'].upper() == input_serial.upper():
            print(item['client'])
            break
    else:
        print('NOT FOUND')
