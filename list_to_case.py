import pyautogui as pg

import base
import keyboard,pyperclip
from screen_name_and_text import *
import codecs

class Base:
    @staticmethod
    def start_authorization_srvmod():
        """Авторизация в SrvMod"""
        #pyperclip.copy(text)
        #keyboard.press_and_release('ctrl + v')
        base.run_exe_42(base.path_42)
        login_and_password = base.search_locate_coordinates(base_screen['Логин пароль'])
        assert login_and_password
        login = base.search_locate_coordinates(base_screen['Имя пользователя'])
        assert login
        pg.click(login)
        keyboard.write(text['Имя пользователя'])
        password = base.search_locate_coordinates(base_screen['Пароль'])
        assert password
        pg.click(password, duration=0.1)
        keyboard.write(text['Пароль'])
        ok = base.search_locate_coordinates(base_screen['Ок,окна логина'])
        pg.click(ok)
        return base.search_locate_coordinates(base_screen['Шапка SrvMod'])

    @staticmethod
    def exit_srvmod_cross():
        """Выход из SrvMod крестом"""
        out = base.search_locate_coordinates(base_screen['Крестик выхода'])
        print('выход')
        pg.click(out)
        assert base.search_locate_coordinates(base_screen['Шапка SrvMod'], time_search=2) == False
        return True


class ThreeStripes:
    @staticmethod
    def block_and_f12():
        """Три полоски -> Блокировка и F12"""
        three_stripes = base.search_locate_coordinates(base_screen['Три полоски'])
        assert three_stripes
        pg.click(three_stripes)
        block = base.search_locate_coordinates(three_stripes_screen['Блокировка и F12'])
        assert block
        pg.click(block)
        assert base.search_locate_coordinates(three_stripes_screen['Требуется подтверждение'])
        password = base.search_locate_coordinates(three_stripes_screen['Пароль'])
        assert password
        pg.click(password)
        keyboard.write(text['Пароль'])
        pg.click(base.search_locate_coordinates(three_stripes_screen['Ввод']))
        assert base.search_locate_coordinates(base_screen['Шапка SrvMod'])
        pg.press('F12')
        assert (base.search_locate_coordinates(three_stripes_screen['Требуется подтверждение'])), \
            'Не выходит из SrvMod при нажатии F12'
        return True

    @staticmethod
    def exit_srvmod_exit():
        """Выход из SrvMod кнопкой выход"""
        three_stripes = base.search_locate_coordinates(base_screen['Три полоски'])
        assert three_stripes
        pg.click(three_stripes)
        out = base.search_locate_coordinates(three_stripes_screen['Выход'])
        pg.click(out)
        assert not base.search_locate_coordinates(base_screen['Шапка SrvMod'], time_search=2)
        return True

    @staticmethod
    def about_the_program():
        three_stripes = base.search_locate_coordinates(base_screen['Три полоски'])
        assert three_stripes
        pg.click(three_stripes)
        about = base.search_locate_coordinates(three_stripes_screen['О программе'])
        assert about
        pg.click(about)
        about_win = base.search_locate_coordinates(three_stripes_screen['О программе окно'])
        assert about_win
        out = base.search_locate_coordinates(three_stripes_screen['О программе закрыть'], confidence=0.8)
        assert out
        pg.click(out)
        return not base.search_locate_coordinates(three_stripes_screen['О программе окно'], time_search=2)