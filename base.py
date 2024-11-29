import ctypes
import logging
import os
from time import sleep

import pyautogui as pg

path_42 = 'c:/Users/NASTENKO/Desktop/3CardF/v42/SrvMod_42.lnk'


def get_language():
    """Проверка языка системы, en или ru
    :param lang: язык который нужен, по умолчанию en"""
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    if hex(pf(0)) == '0x4190419':
        return 'ru'
    if hex(pf(0)) == '0x4090409':
        return 'en'


def run_exe_42(exe_path):
    os.startfile(exe_path)
    return 'Ок'


class LogsTestInfo:
    @staticmethod
    def logs_error_false(name_test):
        """Логирование проваленных тестов"""
        logging.error(f"{name_test} ПРОВАЛЕН")

    @staticmethod
    def logs_info_true(name_test):
        """Логирование успешных тестов"""
        logging.info(f"{name_test} ПРОЙДЕН")

    @staticmethod
    def log_start(name_test):
        logging.info(f"{name_test} Старт")

    @staticmethod
    def log_finish(name_test):
        logging.info(f"{name_test} Конец")


class SearchScreen:
    @staticmethod
    def search_locate_coordinates(name_screen, time_search=5, confidence=0.95):
        """
        Поиск координат и проверка на отсутствие за выставленное время.
        :param name_screen: Строка, путь к скриншоту после Screen/
        :param time_search: Время поиска скриншота
        :param confidence: Точность поиска, по умолчанию 0.95
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
                    return False

    @staticmethod
    def search_assert_and_log_and_click(name_screen, time_search=5, confidence=0.95):
        """
        Проверка логирование и нажатие на клавишу.
        :param name_screen: Строка, путь к скриншоту после Screen/
        :param time_search: Время поиска скриншота
        :param confidence: Точность поиска, по умолчанию 0.95
        :return: Координаты при успешном поиске, FAlSE если не найден
        """
        data = SearchScreen().search_locate_coordinates(name_screen, time_search, confidence)
        assert data, logging.error(f"Скрин по пути '{name_screen}' НЕНАЙДЕН")
        logging.info(f"Скрин '{name_screen}' по пути  НАЙДЕН")
        pg.click(data, duration=0.1)
