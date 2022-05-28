# uncompyle6 version 3.8.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)]
# Embedded file name: autojacks.py
import keyboard
from time import sleep as wait
from num2words import num2words
print('[1] ONE!\n[2] One.\n[3] O N E ONE!')
inp = input('Enter Selection: ')
am = input('Enter number of JJs: ')
if inp == '1':
    print('Waiting 10 seconds to start!')
    wait(2)
    for i in range(int(am)):
        keyboard.press('space')
        wait(0.1)
        keyboard.release('space')
        keyboard.press_and_release('/')
        wait(1)
        wrd = num2words(i + 1).upper()
        if '-' in wrd:
            wrd = wrd.replace('-', ' ')
        if 'AND' in wrd:
            wrd = wrd.replace('AND', '')
        keyboard.write(wrd + '!')
        wait(1.5)
        keyboard.press_and_release('enter')
        wait(2)

else:
    if inp == '2':
        print('Waiting 10 seconds to start!')
        wait(2)
        for i in range(int(am)):
            keyboard.press('space')
            wait(0.1)
            keyboard.release('space')
            keyboard.press_and_release('/')
            wait(1)
            wrd = num2words(i + 1).title()
            if '-' in wrd:
                wrd = wrd.replace('-', ' ')
            keyboard.write(wrd + '.')
            wait(1)
            keyboard.press_and_release('enter')
            wait(2)

    elif inp == '3':
        print('Waiting 10 seconds to start!')
        wait(2)
        for i in range(int(am)):
            for j in num2words(i + 1):
                keyboard.press('space')
                wait(0.1)
                keyboard.release('space')
                keyboard.press_and_release('/')
                wait(1)
                print(j)
                keyboard.write(j.upper())
                wait(0.5)
                keyboard.press_and_release('enter')
                wait(0.5)

            keyboard.press('space')
            wait(0.1)
            keyboard.release('space')
            keyboard.press_and_release('/')
            wait(1)
            wrd = num2words(i + 1).upper()
            if '-' in wrd:
                wrd = wrd.replace('-', ' ')
            keyboard.write(wrd + '!')
            wait(1.5)
            keyboard.press_and_release('enter')
            wait(2)