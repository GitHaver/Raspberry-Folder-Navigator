from os import chdir,system,getcwd,path,listdir,replace,makedirs,remove,scandir
from sys import exit
from pathlib import Path

home = path.expanduser('~')
chdir(home)


if '\\' in getcwd():
    struct = "windows"
    stroke = "\\"
elif '/' in getcwd():
    struct = "linux"
    stroke = "/"


print(f"{struct} detected.)")


def cls():
    if struct == "windows":
        system('cls')
    elif struct == "linux":
        system('clear')


def back():
    menumanager()


def title(title):
    bar = ''
    for i in range(len(title)):
        bar = bar + '-'
    print(bar)
    print(title)
    print(bar)

def takeaction():
    title("Take Action")
    print('1 - Create Folder')
    print('2 - Rename/Move Folder')
    print('3 - Create File')
    print('4 - Rename/Move File')
    print('5 - Back')
    print()
    choice = int(input('Please choose: '))

    if choice == 1:
        print("Please enter a folder name.")
        print("You may enter multiple subdirectories followed by a slash, eg:")
        print(f"new_folder1{stroke}newer_folder2")
        print("Or enter cancel to cancel.")
        name = input(f'{cwd}{stroke}')
        if name.lower() == "cancel":
            takeaction()
        else:
            makedirs(f'{cwd}/{name}')
            print(f"Success, created: {cwd}{stroke}-{name}- ")
            print("Move to directory now?")
            choice = input("Y/n: ")
            if choice.lower() == "y":
                chdir(f'{cwd}{stroke}{name}')
                menumanager()
            else:
                menumanager()

    elif choice == 2:
        print("Please enter the name of a folder to delete.")
        print("You may enter multiple subdirectories followed by a slash, e.g.:")
        print(f"existing_folder{stroke}existing_subfolder{stroke}folder_to_delete")
        print("Or enter cancel to cancel.")
        name = input(f"{cwd}{stroke}")
        if name == "cancel".lower():
            takeaction()
        else:
            remove(f'{cwd}{stroke}{name}')
            print(f"Success, created: {cwd}{stroke}-{name}- ")
            wait = input("Return?")
            menumanager()

    elif choice == 3:
        print("Please enter a file name.")
        print("You may enter multiple subdirectories followed by a slash, e.g.:")
        print(f"existing_folder{stroke}not_existing_folder{stroke}filename.py")
        print("Or enter cancel to cancel.")
        name = input("File name: ")
        if name == "cancel".lower():
            takeaction()
        else:
            with open(f'{cwd}{stroke}{name}', 'w') as fp:
                pass
            print(f"Success, created: {cwd}{stroke}-{name}- ")
            wait = input("Return?")
            menumanager()

    elif choice == 3:
        cls()
        print("Please enter the name of the file you would like to move, rename, or delete: ")
        print("Or enter cancel to cancel.")
        name = input("File name: ")
        if name == "cancel".lower():
            takeaction()
        else:
            cls()
            print()
            print("Please enter the new path of the file including the file, with its new name: ")
            print("This may include folders that do not exist yet, e.g: ")
            print(f"new_dir{stroke}newer_dir{stroke}new_file_name.txt")
            newfile = input(f'{cwd}{stroke}')
            replace(f'{cwd}/{name}', f'{cwd}/{newfile}')

    elif choice == 4:
        back()


def menuchoice(contents):
    choice = int(input("Please choose: "))
    choice -= 1
    choice = contents[choice]
    choice = choice.replace(",","")

    if choice == '<':
        chdir("..")
        menumanager()

    elif choice == "Home":
        chdir(home)
        menumanager()

    elif choice == "Exit":
        exit()

    elif choice == "takeaction":
        takeaction()

    elif choice[0] =='F':
          chdir(choice.lstrip('F'))
          menumanager()

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


def menumanager():
    cls()
    contents = []
    cwd = getcwd()

    f = []
    d = []
    files = [f for f in Path('.').iterdir() if f.is_file()]
    folders = [d for d in Path('.').iterdir() if d.is_dir()]

    count = 0

    title(cwd)

    print("Folders:")
    for folder in folders:
        count += 1
        contents.append(f'F{folder}')
        print(f'{count} - {folder}')
    print()
    print("Files:")
    for file in files:
        count += 1
        contents.append(f'f{file}')
        print(f'{count} - {file}')
    print()
    print("Actions:")
    count +=1
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
    print(f'{count} - {either}')

    menuchoice(contents)

menumanager()



