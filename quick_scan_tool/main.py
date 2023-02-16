#!/usr/bin/python3

import csv
from os import path


def list_to_csv_string(list):
    string = ''
    for idx, item in enumerate(list):
        if idx > 0:
            string += ','
        string += item
    return string


print('\nWelcome to the Resonance Quick Scan tool.\nWhen you are finished, type \'done\' on either input.\n\n')

file_name = input('Enter file name (no extension): ')
file_name += '.csv'

if path.exists(f'./{file_name}'):
    overwrite = input(
        'A file with this name already exists.\nDo you wish to overwrite? [Y/n] ')
    if (overwrite.upper()) != 'Y':
        exit()

row_names = input('\nInsert row names (separated by spaces): ').split()

with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(row_names)

    while True:
        row = []
        for row_name in row_names:
            val = input(f'{row_name}: ')
            row.append(val)
        row_ok = input(
            f'\'{list_to_csv_string(row)}\' -- Ok? [enter/N] ')
        if row_ok.upper() == '':
            writer.writerow(row)
            print('Success!\n')
        else:
            print('Not added\n')
            continue
