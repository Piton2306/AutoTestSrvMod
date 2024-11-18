import os
import time

import pyautogui as pg

path_42 = 'c:/Users/NASTENKO/Desktop/3CardF/v42/SrvMod_42.lnk'
path_screen = f'Screen/'


def run_exe_42(exe_path):
    exe = os.startfile(exe_path)
    return 'Ок'




#run_exe_42(path_42)


def search_locate(name_screen,confidence = 0.8):
    print(path_screen + name_screen)
    time.sleep(2)
    coordinates = pg.locateOnScreen(path_screen + name_screen, confidence=0.8)

    print('2')
    print(coordinates)
    pg.moveTo(coordinates)


search_locate('base/1.png')
print()
