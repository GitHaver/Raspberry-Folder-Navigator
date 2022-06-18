from os import chdir, getcwd, path
from lib.util import title, cls, list_printer, dir_nav_chooser
from pathlib import Path
import sys

home = path.expanduser('~')

try:
    chdir(str(sys.argv[1]))
except IndexError:
    chdir(home)
cwd = getcwd()

if '\\' in getcwd():
    struct = ["windows", "\\"]
elif '/' in getcwd():
    struct = ["linux", "/"]
else:
    print("Operating system not recognized, please fill in the blanks:")
    struct = [input("Operating system: ")]
    print('What symbol is used to divide folders in a filepath?')
    struct.append(input('E.g. In your system, what is the "/" in: "C:/Users/Home": '))


def menu_manager(directory=getcwd()):
    cls()
    chdir(directory)
    contents = []
    title(directory)

    f = []
    d = []

    count = 0
    folders = [d for d in Path(".").iterdir() if d.is_dir()]
    for folder in folders:
        contents.append(f'F{folder}')
        count += 1
    print("Folders:")
    print()
    count = list_printer(folders)

    files = [f for f in Path(".").iterdir() if f.is_file()]
    for file in files:
        contents.append(f'f{file}')
        count += 1
    print()
    print("Files:")
    print()
    count = list_printer(files, count)

    print()
    print("Actions:")
    contents.append('takeaction')
    print(f'{count} - Take Action')
    count += 1
    contents.append('<')
    print(f'{count} - <')
    if home == cwd:
        either = "Exit"
    else:
        either = "Home"
    contents.append(either)
    count += 1
    print(f'{count} - {either}')
    dir_nav_chooser(cwd, contents)


while __name__ == "__main__":
    try:
        menu_manager(getcwd())
    except PermissionError:
        wait = input("You do not have access to this folder, press any key to return to your home directory.")
        menu_manager(home)

