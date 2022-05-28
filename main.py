import keyboard
from colorama import *
import os
from tqdm import tqdm 
from time import sleep
import num2words
import json


# //vars
while True:
    config = open(os.path.join(os.getcwd() , "config.json"), "r")
    configJson = json.loads(config.read())
    charsPerSecond = (configJson["wpm"] * 5) / 60


    # //initial menu
    init()
    os.system('color')
    print(Fore.BLUE+"""
    [1] ONE!
    [2] One.
    [3] O N E ONE!
    """)
    selection = input(Fore.LIGHTMAGENTA_EX + "Enter Selection: ")
    if selection == "1":
        os.system("cls")
        jjCount = input(Fore.LIGHTMAGENTA_EX + "Enter how many JJs': ")
        sleep(1)
        print(Fore.GREEN+ "\n\n")
        for i in tqdm(range(int(jjCount))):
            keyboard.press('space')
            sleep(0.1)
            keyboard.release('space')
            keyboard.press_and_release('/')
            sleep(.1)
            wrd = num2words.num2words(int(i)+1).upper()
            if '-' in wrd:
                wrd = wrd.replace('-', ' ')
            if 'AND' in wrd:
                wrd = wrd.replace('AND', '')
            sleep(len(wrd) / charsPerSecond)
            keyboard.write(wrd + '!')
            sleep(.1)
            keyboard.press_and_release("enter")
            sleep(.5)
    if selection == "2":
        os.system("cls")
        jjCount = input(Fore.LIGHTMAGENTA_EX + "Enter how many JJs': ")
        sleep(1)
        print(Fore.GREEN+ "\n\n")
        for i in tqdm(range(int(jjCount))):
            keyboard.press('space')
            sleep(0.1)
            keyboard.release('space')
            keyboard.press_and_release('/')
            sleep(.1)
            wrd = num2words.num2words(int(i)+1).title()
            if '-' in wrd:
                wrd = wrd.replace('-', ' ')
            sleep(len(wrd) / charsPerSecond)
            keyboard.write(wrd + '.')
            sleep(.1)
            keyboard.press_and_release("enter")
            sleep(.5)
    if selection == "3":
        os.system("cls")
        jjCount = input(Fore.LIGHTMAGENTA_EX + "Enter how many JJs': ")
        sleep(1)
        print(Fore.GREEN+ "\n\n")
        for i in tqdm(range(int(jjCount))):
            wrd = num2words.num2words(int(i)+1).upper()
            for j in wrd:
                keyboard.press('space')
                sleep(0.1)
                keyboard.release('space')
                keyboard.press_and_release('/')
                sleep(.1)
                sleep(len(j) / charsPerSecond)
                keyboard.write(j)
                sleep(.1)
                keyboard.press_and_release("enter")
                sleep(.3)
            sleep(.3)
            keyboard.press('space')
            sleep(0.1)
            keyboard.release('space')
            keyboard.press_and_release('/')
            sleep(.1)
            if '-' in wrd:
                wrd = wrd.replace('-', ' ')
            if 'AND' in wrd:
                wrd = wrd.replace('AND', '')
            sleep(len(wrd) / charsPerSecond)
            keyboard.write(wrd + '!')
            sleep(.1)
            keyboard.press_and_release("enter")
            sleep(.5)
    os.system("cls")