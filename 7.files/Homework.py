import time
import os
import tkinter as tk
from tkinter import filedialog


def select_file_txt():

    file_path = filedialog.askopenfilename(
        filetypes=[('Text files', '*.txt')])
    if not file_path:
        print('Р¤Р°Р№Р» РЅРµ РІС‹Р±СЂР°РЅ')
    return file_path


def create_cook_book(file_path):

    with open(file_path, encoding='utf-8') as file:
        cook_book = dict()
        for txt_string in file.read().split('\n\n'):
            name, _, *args = txt_string.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(
                    lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name,
                           'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
    return cook_book


def create_shop_list(cook_book):

    dishes = input('Р’РІРµРґРёС‚Рµ СЃРїРёСЃРѕРє Р±Р»СЋРґ (С‡РµСЂРµР· Р·Р°РїСЏС‚СѓСЋ): ').split(', ')
    person_count = int(input('Р’РІРµРґРёС‚Рµ РєРѕР»РёС‡РµСЃС‚РІРѕ РїРµСЂСЃРѕРЅ: '))

    denial = False

    if not dishes:
        print_message('РќРµ СѓРєР°Р·Р°РЅ СЃРїРёСЃРѕРє Р±Р»СЋРґ', denial)

    if not person_count:
        print_message('РќРµ СѓРєР°Р·Р°РЅРѕ РєРѕР»РёС‡РµСЃС‚РІРѕ РїРµСЂСЃРѕРЅ', denial)

    if denial:
        time.sleep(1)
        exit()

    shop_list = dict()
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingridients in cook_book[dish_name]:
                if ingridients['ingredient_name'] in shop_list:
                    shop_list[ingridients['ingredient_name']]['quantity'] = shop_list[ingridients['ingredient_name']
                                                                                      ]['quantity'] + ingridients['quantity'] * person_count
                else:
                    new_element_list = dict()
                    new_element_list['measure'] = ingridients['measure']
                    new_element_list['quantity'] = ingridients['quantity']
                    shop_list[ingridients['ingredient_name']
                              ] = new_element_list
        else:
            print(f'\n"Р‘Р»СЋРґР° {dish_name} РЅРµС‚ РІ СЃРїРёСЃРєРµ!"\n')
    return shop_list


def print_message(message, denial=True):
    print('РќРµ СѓРєР°Р·Р°РЅ СЃРїРёСЃРѕРє Р±Р»СЋРґ')
    denial = True


def get_union_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        print('Р¤Р°Р№Р» РЅРµ РІС‹Р±СЂР°РЅ')
        time.sleep(1)
        exit()

    os.chdir(folder_path)
    file_list = os.listdir('.')

    union_files = []
    for file in file_list:
        if file.endswith('result.txt'):
            continue
        elif file.endswith('.txt'):
            union_files.append(file)

    union_files.sort(key=lambda path: sum(
        1 for line in open(path, 'r', encoding='utf-8')))

    with open('result.txt', 'w') as result_file:
        for file in union_files:

            with open(file, 'r', encoding='utf-8') as read_file:

                lines = read_file.readlines()
                result_file.write(f'{file}\n{len(lines)}\n')
                result_file.writelines(lines)


if __name__ == '__main__':

    file_path = select_file_txt()
    if file_path == '':
        time.sleep(1)
        exit()
    cook_book = create_cook_book(file_path)
    print(cook_book)
    print('Р—Р°РґР°РЅРёРµ 1--------------')
    time.sleep(1)
    shop_list = create_shop_list(cook_book)
    print(shop_list)
    print('Р—Р°РґР°РЅРёРµ 2--------------')
    time.sleep(1)

    get_union_files()
    print('Р—Р°РґР°РЅРёРµ 3--------------')
    time.sleep(1)
    exit()
