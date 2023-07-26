import random

from art import tprint

from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style
from math import ceil, log2


def is_valid(text):
    return text.isdigit and 1 <= int(text) <= 100

while True:

    print('''Чтобы начать игру нажмите 1,
Чтобы закрыть игру нажмите 2''')

    response = int(input())
    if response == 2:
        exit()

    response_maxnum = int(input("Введите правую границу для случайного числа: "))
    secret_num = random.randint(1, response_maxnum)
    max_tries = ceil(log2(response_maxnum))

    tries = 0

    tprint("guess  number")
    print(f"Вам дано {max_tries} попыток")


    while tries < max_tries:
        num = input(Fore.YELLOW + "Введите число от 1 до 100: ")
        tries += 1

        if is_valid(num):
            if int(num) == secret_num:

                print(Fore.GREEN + f"Вы угадали число за, {tries} попыток")
                input(Fore.RED + "Чтобы закрыть программу нажмите enter...")
                break
            elif int(num) < secret_num:
                print(Fore.YELLOW + "Выше число меньше загаданного")
            elif int(num) > secret_num:
                print(Fore.BLACK + "Ваше число больше загаданного")
        else:
            print(Fore.BLUE + "Попробуте ввести другое целое число от 1 до 100")
    else:
        print(Fore.RED + "Вы проиграли!")





