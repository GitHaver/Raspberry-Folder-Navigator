from os import chdir, system, getcwd, path, listdir, replace, makedirs, remove, scandir
from lib.util import title, cls, list_printer
from sys import exit
from pathlib import Path

home = path.expanduser('~')
chdir(home)

if '\\' in getcwd():
    struct = ["windows", "\\"]
elif '/' in getcwd():
    struct = ["linux", "/"]
else:
    print("Operating system not recognized, please fill in the blanks:")
    struct = [input("Operating system: ")]
    print('What symbol is used to divide folders in a filepath?')
    struct.append(input('E.g. In your system, what is the "/" in: "C:/Users/Home": '))


def back():
    menu_manager()


def take_action(cwd):
    title("Take Action", 1)
    half_path = cwd + {struct[2]}
    print('1 - Create Folder')
    print('2 - Rename/Move Folder')
    print('3 - Create File')
    print('4 - Rename/Move File')
    print('5 - Back')
    print()
    choice = int(input('Please choose: '))

    if choice == 1:
        print("Please enter a folder name.")
        print(f'You may enter multiple subdirectories separated by {struct[2]}, eg:')
        print(f"new_folder1{struct[2]}newer_folder2")
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
                menu_manager()
            else:
                menu_manager()

    elif choice == 2:
        print("Please enter the name of a folder to delete.")
        print("You may enter multiple subdirectories followed by a slash, e.g.:")
        print(f"existing_directory{struct[2]}existing_subdirectory{struct[2]}folder_to_delete")
        print("Or enter cancel to cancel.")
        name = input(f"{half_path}")
        if name == "cancel".lower():
            take_action()
        else:
            remove(f'{half_path}{name}')
            print(f"Success, created: {half_path}--{name}-- ")
            wait = input("Return?")
            menu_manager()

    elif choice == 3:
        print("Please enter a file name.")
        print("You may enter multiple subdirectories followed by a slash, e.g.:")
        print(f"existing_folder{struct[2]}not_existing_folder{struct[2]}filename.py")
        print("Or enter cancel to cancel.")
        name = input("File name: ")
        if name == "cancel".lower():
            take_action(cwd)
        else:
            with open(f'{half_path}{name}', 'w') as fp:
                pass
            print(f"Success, created: {half_path}-{name}- ")
            wait = input("Return?")
            menu_manager()

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
            print(f"new_dir{struct[2]}newer_dir{struct[2]}new_file_name.txt")
            newfile = input(f'{half_path}')
            replace(f'{half_path}', f'{half_path}{newfile}')

    elif choice == 4:
        back()


def menu_choice(contents):
    choice = int(input("Please choose: "))
    choice -= 1
    choice = contents[choice]
    choice = choice.replace(",","")

    if choice == '<':
        chdir("..")
        menu_manager()

    elif choice == "Home":
        chdir(home)
        menu_manager()

    elif choice == "Exit":
        exit()

    elif choice == "take_action":
        take_action(cwd)

    elif choice[0] =='F':
          chdir(choice.lstrip('F'))
          menu_manager()

    elif choice[0] =='f':
        choice = choice.lstrip('f')

        if '.py' in choice:
            print(f"1. Run {choice}")
            print(f"2. Edit {choice}")
            choice2=input("Please choose: ")
            if choice2 == '1':
                system(f"python {choice}")
            elif choice2 == '2':
                system(f"sudo nano {choice}")

        elif '.js' in choice:
            print(f"1. Run {choice}")
            print(f"2. Edit {choice}")
            choice2=input("Please choose: ")
            if choice2 == '1':
                system(f"node {choice}")
            elif choice2 == '2':
                system(f"sudo nano {choice}")
            else:
                system(f"sudo nano {choice}")

        else:
            print(f"No handler found for {choice} - sending to Nano")
            system(f"sudo nano {choice}")


def menu_manager():
    cls(struct)
    contents = []
    cwd = getcwd()

    f = []
    d = []
    count = 0

    folders = [d for d in Path('.').iterdir() if d.is_dir()]
    for folder in folders:
        count += 1
        contents.append(f'F{folder}')

    files = [f for f in Path('.').iterdir() if f.is_file()]
    for file in files:
        count += 1
        contents.append(f'f{file}')

    title(cwd)

    print("Folders:")
    print()
    count = list_printer(folders)
    print("Files:")
    print()
    list_printer(files, count)

    count = 0
    print()
    print("Actions:")
    count += 1
    contents.append('takeaction')
    print(f'{count} - Take Action')
    count += 1
    contents.append('<')
    print(f'{count} - <')
    if path.expanduser('~') == cwd:
        either = "Exit"
    else:
        either = "Home"
    contents.append(either)
    count += 1

    menu_choice(contents)

while __name__ == "__main__":
    menu_manager()



