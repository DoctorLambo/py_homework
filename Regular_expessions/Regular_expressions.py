from pprint import pprint

import csv
from re import sub

def read_file(file_name):
    with open(file_name, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def format_list(contacts_list):
    contacts_list = format_phone_number(contacts_list)
    contacts_list = format_full_name(contacts_list)
    return contacts_list

def format_phone_number(contacts_list):
    
    pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    return format_raw(contacts_list, pattern_raw, pattern_new)

def format_full_name(contacts_list):
    pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    pattern_new = r'\1\3\10\4\6\9\7\8'
    return format_raw(contacts_list, pattern_raw, pattern_new)

def format_raw(format_list, pattern_raw, new_pattern):
    
    result = list()
    for card in format_list:
        formated_row = ','.join(card)
        formatted_card = sub(pattern_raw, new_pattern, formated_row)
        result.append(formatted_card.split(','))
    return result

def join_duplicate(contacts_list):
   
    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] is '':
                    i[2] = j[2]
                if i[3] is '':
                    i[3] = j[3]
                if i[4] is '':
                    i[4] = j[4]
                if i[5] is '':
                    i[5] = j[5]
                if i[6] is '':
                    i[6] = j[6]
    contacts_list_updated = list()
    for card in contacts_list:
        if card not in contacts_list_updated:
            contacts_list_updated.append(card)
    return contacts_list_updated                       


def safe_file(contacts_list):
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)

if __name__ == '__main__':
    contacts_list = read_file('phone_book_raw.csv')
    contacts_list = format_list(contacts_list)
    contacts_list = join_duplicate(contacts_list)
    safe_file(contacts_list)
