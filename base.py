import os
import time
from time import sleep
import pyautogui as pg

path_42 = 'c:/Users/NASTENKO/Desktop/3CardF/v42/SrvMod_42.lnk'


def run_exe_42(exe_path):
    os.startfile(exe_path)
    return 'Ок'


def search_locate_coordinates(name_screen, time_search=5, confidence=0.95):
    """"
    :param name_screen: Строка, путь к скриншоту после Screen/
    :param time_search: Время поиска скриншота
    :param confidence: Точность поиска, по умолчанию 0.8
    :return: Координаты при успешном поиске, FAlSE если не найден
    """
    count = 0
    while True:
        try:
            coordinates = pg.locateOnScreen(name_screen, confidence=confidence)
            # print(f'В течении {count} секунд координаты {name_screen} найдены')
            return coordinates
        except pg.ImageNotFoundException:
            count += 0.5
            sleep(0.5)
            if count == time_search:
                # print(f'В течении {count} секунд координаты {name_screen} не найдены')
                return False
