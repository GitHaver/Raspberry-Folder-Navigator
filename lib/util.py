from os import system
from math import ceil

def title(name, opt=1):
    bar = ''
    for i in range(len(name)):
        bar += '-'
    if opt == 1:
        print(bar)
    print(name)
    print(bar)


def cls(struct):
    if struct[1] == "windows":
        system('cls')
    elif struct[1] == "linux":
        system('clear')


def list_printer(items, count=0):
    count = count
    list_a = []
    for item in items:
        item = f'[{count}] - {item}'
        length = len(item)
        if len(item) >= length:
            longest = length
        list_a.append(item)
        count += 1
    longest += 12
    items = []
    for item in list_a:
        chars = len(item)
        difference_from_longest = longest - chars
        space = ' ' * difference_from_longest
        items.append(item + space)
    columns = ceil(len(items) / 6)
    rows = columns
    count = 0
    record_id = 0
    row_1 = ""
    while count < columns:
        try:
            row_1 = row_1 + items[record_id]
            count += 1
            record_id += 5
        except IndexError:
            break

    count = 0
    record_id = 1
    row_2 = ""
    while count < columns:
        try:
            row_2 = row_2 + items[record_id]
            count += 1
            record_id += 5
        except IndexError:
            break

    count = 0
    record_id = 2
    row_3 = ""
    while count < columns:
        try:
            row_3 = row_3 + items[record_id]
            count += 1
            record_id += 5
        except IndexError:
            break

    count = 0
    record_id = 3
    row_4 = ""
    while count < columns:
        try:
            row_4 = row_4 + items[record_id]
            count += 1
            record_id += 5
        except IndexError:
            break

    count = 0
    record_id = 4
    row_5 = ""
    while count < columns:
        try:
            row_5 = row_5 + items[record_id]
            count += 1
            record_id += 5
        except IndexError:
            break

    count = 0
    record_id = 5
    row_6 = ""
    while count < columns:
        try:
            row_6 = row_6 + items[record_id]
            count += 1
            record_id += 5
        except IndexError:
            break

    print(row_1)
    print(row_2)
    print(row_3)
    print(row_4)
    print(row_5)
    print(row_6)
    return len(items)





