import pyautogui as pag
from getpass import getpass
import sys
import json
import requests
import keyboard
import time
import random
import webbrowser
from os import system, name
from colorama import Fore, Back, Style


def clear():
    if name == 'nt':
        _ = system('cls')


def add():
    try:
        namesFile = open("names.txt", "r")
    except:
        print(Style.BRIGHT + Fore.LIGHTRED_EX +
              "Could not open names.txt - please make sure this file exists")
        exit()

    namesData = namesFile.read()
    names = namesData.strip().split("\n")

    print(Style.BRIGHT + Fore.LIGHTRED_EX + "Retrieved names from names.txt\n")

    print(Style.BRIGHT + Fore.LIGHTRED_EX +
          ":: Click enter when your mouse is over the 'Add Friend Button' ::")
    if keyboard.read_key() == "enter":
        addFriend = pag.position()
        print(f"Cords captured: {addFriend}")
    time.sleep(1)
    print(":: Click enter when your mouse is over the 'Close Button' ::")
    if keyboard.read_key() == "enter":
        close = pag.position()
        print(f"Cords captured: {close}")
    time.sleep(1)
    print(":: Click enter when your mouse is over the 'Find Friend Search Bar' ::")
    if keyboard.read_key() == "enter":
        searchBar = pag.position()
        print(f"Cords captured: {searchBar}")
    time.sleep(1)
    print(":: Click enter when your mouse is over the 'Clear Friend Bar' ::")
    if keyboard.read_key() == "enter":
        clearText = pag.position()
        print(f"Cords captured: {clearText}")
    time.sleep(1)
    print(":: Click enter when your mouse is over the 'First Add Button' ::")
    while True:
        if keyboard.read_key() == "enter":
            firstAdd = pag.position()
            print(f"Cords captured: {firstAdd}")
            break
        else:
            continue
    clear()

    def adder(name):

        # move to search bar
        pag.moveTo(searchBar[0], searchBar[1], 0.5)
        pag.click()
        time.sleep(2)

        # write out name
        pag.typewrite(name, interval=0.10)
        time.sleep(2)

        # move to first add, then add
        pag.moveTo(firstAdd[0], firstAdd[1], 0.5)
        pag.click()
        time.sleep(2)
        pag.click()
        time.sleep(2)
        pag.click()
        time.sleep(2)
        pag.click()
        time.sleep(2)
        pag.click()
        time.sleep(2)
        pag.click()
        time.sleep(2)
        pag.click()
        time.sleep(2)
        pag.click()
        time.sleep(2)
        pag.click()
        time.sleep(2)

        # clears search bar
        pag.moveTo(clearText[0], clearText[1], 0.5)
        pag.click()

    print("will cycle through your name list randomly\n\n")
    time.sleep(3)

    for name in names:
        print("Doing: {0}".format(name))
        adder(name)
        time.sleep(1)


def sendsnap():
    print(Style.BRIGHT + Fore.LIGHTRED_EX +
          'How many cycles would you like to use? (1200 score per cycle): ')
    print(Fore.CYAN + '\n\n\n\n\nSnapify> ', end='')
    amount = float(input(Fore.WHITE + ''))
    clear()
    print(Style.BRIGHT + Fore.LIGHTRED_EX +
          ":: Click enter when your mouse is over the 'Camera Button' ::")
    if keyboard.read_key() == "enter":
        CameraButton = pag.position()
        print(f"Cords captured: {CameraButton}")
    time.sleep(1)
    print(":: Take a picture then click enter when your mouse is over the 'Send To Button' ::")
    if keyboard.read_key() == "enter":
        SendToButton = pag.position()
        print(f"Cords captured: {SendToButton}")
    time.sleep(1)
    print(":: Click on 'Send To Button' then click enter when your mouse is over the 'Last Snap Button' ::")
    if keyboard.read_key() == "enter":
        LastSnapButton = pag.position()
        print(f"Cords captured: {LastSnapButton}")
    time.sleep(1)
    print(":: Click enter when your mouse is over the 'Send Snap Arrow' ::")
    if keyboard.read_key() == "enter":
        SendSnapArrow = pag.position()
        print(f"Cords captured: {SendSnapArrow}")
    time.sleep(1)
    print(":: Click enter when your mouse is over the 'Camera Logo at the bottom center' ::")
    if keyboard.read_key() == "enter":
        CameraLogo = pag.position()
        print(f"Cords captured: {CameraLogo}")
    # countdown screen
    TimeToHomePage = 15
    while TimeToHomePage >= 0:
        clear()
        print(
            f'You have {TimeToHomePage} seconds to go back to the snapchat homescreen before the boost begins.')
        time.sleep(1)
        TimeToHomePage -= 1
    clear()
    print(
        f"Started boosting! Please don't turn off your phone or close this window while it's running. This will run for {amount} cycle('s)")
    print('\n\n\n\n\n\n')
    while amount > 0:
        # move to camera button and record for one minute
        pag.moveTo(CameraButton[0], CameraButton[1], 0.5)
        pag.mouseDown()
        time.sleep(60)
        pag.mouseUp()

        # move to send to button and click
        pag.moveTo(SendToButton[0], SendToButton[1], 0.5)
        pag.click()

        # move to last snap and click
        pag.moveTo(LastSnapButton[0], LastSnapButton[1], 0.5)
        pag.click()

        # move to send snap button and click
        pag.moveTo(SendToButton[0], SendToButton[1], 0.5)
        pag.click()

        # move to send snap arrow and click
        pag.moveTo(SendSnapArrow[0], SendSnapArrow[1], 0.5)
        pag.click()

        # move to camera logo and click
        pag.moveTo(CameraLogo[0], CameraLogo[1], 0.5)
        pag.click()

        amount -= 1
        print(f'Finished one cycle. {amount} left to go.')
    clear()
    print(Fore.GREEN + 'Finished Boosting. Thanks for using our tool.')
    print(Fore.MAGENTA + '\n\nPlease check us out at:\n\nQuessts: https://cracked.to/Quessts\nANG: https://cracked.to/ANG', end='')
    getpass(Fore.WHITE + '')
    sys.exit()


clear()


while True:
    print(Style.BRIGHT + Fore.LIGHTRED_EX + """

                                        
    %(                              #%  
    %###                          ###%  
    %%%%#####  @@@/@@@/@@@, #####%##%       ███████╗███╗   ██╗ █████╗ ██████╗ ██╗███████╗██╗   ██╗
     %&%%%#%&@              @&%%#%%&%       ██╔════╝████╗  ██║██╔══██╗██╔══██╗██║██╔════╝╚██╗ ██╔╝  
        %&&%                 %%%&%          ███████╗██╔██╗ ██║███████║██████╔╝██║█████╗   ╚████╔╝ 
          @@                  @%            ╚════██║██║╚██╗██║██╔══██║██╔═══╝ ██║██╔══╝    ╚██╔╝  
          @@                  @&            ███████║██║ ╚████║██║  ██║██║     ██║██║        ██║   
      *@/ @@                  @* @@         ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝        ╚═╝  
     ,@@                         &@@    
          /                   @@           #1 Free snapchat booster Developed by ANG#6166 and Quessts#2071
         @@                    @%       
       @@                       &@#         V1.0
  %@@@*                            @@@@*
  &@@@@(                          @@@@@ 
       @@@@@@@             #@@@@@@@     
               @@@#@@(##@@(   
                           
""")

    print(
        'Select module:\n\n\n\n1) Add Friends\n\n2) Boost\n\n\n ')
    print(Fore.CYAN + 'Snapify> ', end='')
    option = input(Fore.WHITE + '')

    if option == '1':
        clear()
        add()
    elif option == '2':
        while True:
            clear()
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  "If you know how to use this type 'yes' if you don't type 'no'\n\n")
            print(Fore.CYAN + 'Snapify> ', end='')
            watchvid = input(Fore.WHITE + '').lower()
            if watchvid == 'yes':
                clear()
                sendsnap()
            elif watchvid == 'no':
                clear()
                webbrowser.open_new('https://youtu.be/vp_jK4tBMVI')
                sendsnap()
            else:
                getpass(Style.BRIGHT + Fore.LIGHTRED_EX +
                        'Error. You inserted an invalid option. Please try again.')
                clear()
                continue
    else:
        getpass(Style.BRIGHT + Fore.LIGHTRED_EX +
                'Error. You inserted an invalid option. Please try again.')
        continue
