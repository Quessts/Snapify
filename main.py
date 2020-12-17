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

    anchorNames = ["Add Friend", "Close", "Add Friend Search Bar",
                   "Clear Friend Bar", "First Add Button"]
    anchors = []

    anchorsFulfilled = 0
    anchorsRequired = len(anchorNames)

    print(":: Click enter when your mouse is over '{0}' ::".format(
        anchorNames[anchorsFulfilled]))

    while anchorsFulfilled != anchorsRequired:
        if keyboard.read_key() == "enter":
            mousePositionNow = pag.position()
            anchors.append(mousePositionNow)
            print("Successfully captured mouse coordinates.\n")
            anchorsFulfilled += 1
            if anchorsFulfilled == anchorsRequired:
                break
            print(":: Click enter when your mouse is over '{0}' ::".format(
                anchorNames[anchorsFulfilled]))
            time.sleep(1)

    print("Cords captured: {0}".format(anchors))

    def dragDown(px, time=0.5):
        now = pag.position()
        pag.dragTo(now[0], now[1]+px, time, button='left')

    def adder(name):
        global anchors
        addFriend, close, searchBar, clearText, firstAdd = anchors

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

        #
        # Dragging down, to remove
        dragDown(500)

        # move back to the add area
        pag.moveTo(addFriend[0], addFriend[1], 0.5)
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

        print('\n\n\n\n\n\n')
        print(f'Finished one cycle. {amount} left to go.')
        amount -= 1
    clear()
    print(Fore.GREEN + 'Finished Boosting. Thanks for using our tool.')
    print(Fore.MAGENTA + '\n\nPlease check us out at:\n\nQuessts: https://cracked.to/Quessts\nANG: https://cracked.to/ANG', end='')
    getpass(Fore.WHITE + '')
    exit()


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
                webbrowser.open_new('##')
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
