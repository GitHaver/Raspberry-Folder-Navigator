from os import chdir, system, path, replace, makedirs, remove, getcwd
from math import ceil
import sys

home = path.expanduser('~')

if '\\' in getcwd():
    struct = ["windows", "\\"]
elif '/' in getcwd():
    struct = ["linux", "/"]
else:
    print("Operating system not recognized, please fill in the blanks:")
    struct = [input("Operating system: ")]
    print('What symbol is used to divide folders in a filepath?')
    struct.append(input('E.g. In your system, what is the "/" in: "C:/Users/Home": '))


def title(name, opt=1):
    bar = ''
    for i in range(len(str(name))):
        bar += '-'
    if opt == 1:
        print(bar)
    print(name)
    print(bar)


def cls():
    if struct[0] == "windows":
        system('cls')
    elif struct[0] == "linux":
        system('clear')


def longest_item_in_list(item_list):
    longest = 0
    for item in item_list:
        if len(item) > longest:
            longest = len(item)
    return longest


def list_item_shortener(items, max_chars):
    shortened_items = []
    index = (2 * (int(ceil(max_chars / 5)))) - 1
    negative_index = 0 - index
    word_limit = 8
    for unit in items:
        unit = str(unit)
        shortened_words = ""
        if len(unit) > max_chars:
            if len(unit.split()) > 1:
                word_shortened = 0
                for word in unit.split():
                    if len(word) >= word_limit:
                        word = word[:3] + "~ "
                        shortened_words += word
                        word_shortened = 1
                    else:
                        shortened_words += word + " "
                if word_shortened == 0:
                    unit = unit[:index] + "~" + unit[negative_index:]
                else:
                    unit = shortened_words[:-1]
                    word_shortened = 0
            else:
                unit = unit[:index] + "~" + unit[negative_index:]
        shortened_items.append(unit)
    return shortened_items


def list_printer(items, count=0):
    debugger = 0
    debug = "\n"
    if count == 0:
        debug += "Count = 0\n"
    else:
        debug += "Count = " + str(count) + "\n"

    formatted_items = []
    items_per_row = 5
    max_chars = 20

    for item in list_item_shortener(items, max_chars):
        item = f'{count}| {item}'
        formatted_items.append(item)
        count += 1

    debug += "Count after list_item_shortener loop = " + str(count) + "\n"

    longest = longest_item_in_list(formatted_items)
    lengthened_items = []
    for item in formatted_items:
        lengthened_items.append(item + (" " * ((longest - len(item)) + 1)))

    number_of_rows = ceil(len(lengthened_items) / items_per_row)

    list_index = 0
    row_iteration = 0
    debug += "Beginning large row loop:"
    while row_iteration < number_of_rows:
        debug += "\n\t"
        row = ""
        #debug += "Beginning row " + str(row_iteration) + " loop: \n \t"
        item_index = row_iteration
        item_loop = 0
        while item_loop < items_per_row:
            try:
                row += (lengthened_items[item_index])
                item_index += number_of_rows
            except IndexError:
                break

            item_loop += 1
            list_index += 1
        debug += "\tRow " + str(row_iteration) + " finished: " + row
        #debug += "Ending row " + str(row_iteration) + " loop."
        row_iteration += 1
        print(row)
    debug += "\n Ending outer while loop."
    if debugger == 1:
        print(debug)
    return count


def take_action(cwd):
    cls()
    title("Take Action:", 0)
    title(cwd, 0)
    half_path = cwd + struct[1]
    print('1 - Create Folder')
    print('2 - Rename/Move Folder')
    print('3 - Create File')
    print('4 - Rename/Move File')
    print('5 - Back')
    print()
    choice = int(input('Please choose: '))

    if choice == 1:
        print("Please enter a folder name.")
        print(f'You may enter multiple subdirectories separated by {struct[1]}, eg:')
        print(f"new_folder1{struct[1]}newer_folder2")
        print("Or enter cancel to cancel.")
        name = input(f'{half_path}')
        if name.lower() == "cancel":
            take_action(cwd)
        else:
            full_path = half_path + name
            makedirs(f'{full_path}')
            print(f"Success, created: {half_path}--{name}-- ")
            print("Move to directory now?")
            choice = input("Y/n: ")
            if choice.lower() == "y":
                chdir(f'{full_path}')
                return
            else:
                return

    elif choice == 2:
        print("Please enter the name of a folder to delete.")
        print("You may enter multiple subdirectories followed by a slash, e.g.:")
        print(f"existing_directory{struct[1]}existing_subdirectory{struct[1]}folder_to_delete")
        print("Or enter cancel to cancel.")
        name = input(f"{half_path}")
        if name == "cancel".lower():
            take_action(cwd)
        else:
            remove(f'{half_path}{name}')
            print(f"Success, created: {half_path}--{name}-- ")
            wait = input("Return?")
            menu_manager()

    elif choice == 3:
        print("Please enter a file name.")
        print("You may enter multiple subdirectories followed by a slash, e.g.:")
        print(f"existing_folder{struct[1]}not_existing_folder{struct[1]}filename.py")
        print("Or enter cancel to cancel.")
        name = input("File name: ")
        if name == "cancel".lower():
            take_action(cwd)
        else:
            with open(f'{half_path}{name}', 'w') as fp:
                pass
            print(f"Success, created: {half_path}-{name}- ")
            return

    elif choice == 3:
        print("Please enter the name of the file you would like to move, rename, or delete: ")
        print("Or enter cancel to cancel.")
        name = input("File name: ")
        if name == "cancel".lower():
            take_action(cwd)
        else:
            print()
            print("Please enter the new path of the file including the file, with its new name: ")
            print("This may include folders that do not exist yet, e.g: ")
            print(f"new_dir{struct[1]}newer_dir{struct[1]}new_file_name.txt")
            newfile = input(f'{half_path}')
            replace(f'{half_path}', f'{half_path}{newfile}')

    elif choice == 4:
        back()


def dir_nav_chooser(cwd, choices):
    choice = int(input(f'{cwd}: '))
    chosen_item = choices[choice]
    if chosen_item == '<':
        chdir("..")
        return

    elif chosen_item == "Exit":
        sys.exit()

    elif chosen_item == "Home":
        chdir(home)
        return

    elif chosen_item == "takeaction":
        take_action(cwd)
        return

    elif chosen_item[0] == 'F':
        item = chosen_item.lstrip('F')
        chdir(item)
        return

    elif chosen_item[0] =='f':
        choice = chosen_item.lstrip('f')
        file_handler(choice)


def file_handler(choice):
    if '.py' in choice:
        print(f"1. Run {choice}")
        print(f"2. Edit {choice}")
        choice2 = input("Please choose: ")
        if choice2 == '1':
            system(f"python {choice}")
        elif choice2 == '2':
            system(f"sudo nano {choice}")

    elif '.js' in choice:
        print(f"1. Run {choice}")
        print(f"2. Edit {choice}")
        choice2 = input("Please choose: ")
        if choice2 == '1':
            system(f"node {choice}")
        elif choice2 == '2':
            system(f"sudo nano {choice}")
        else:
            system(f"sudo nano {choice}")

    else:
        print(f"No handler found for {choice} - sending to Nano")
        system(f"sudo nano {choice}")