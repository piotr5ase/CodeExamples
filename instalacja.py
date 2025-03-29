# pip install emoji
import os
import emoji
from termcolor import colored
from colorama import Fore, Back, Style, just_fix_windows_console, init

os.system('color')
just_fix_windows_console()
init()
print(emoji.emojize(':flying_saucer:'))
print(
    'ALL', colored('ahu', 'red'), colored('Akh', 'blue'), colored('bar', 'red')
)
print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
