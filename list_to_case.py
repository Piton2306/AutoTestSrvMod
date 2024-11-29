import keyboard
import pyautogui as pg

import base
from screen_name_and_text import *

ss = base.SearchScreen()


class Base:
    @staticmethod
    def start_authorization_srvmod():
        """Авторизация в SrvMod"""
        # pyperclip.copy(text)
        # keyboard.press_and_release('ctrl + v')
        base.run_exe_42(base.path_42)
        login_and_password = ss.search_locate_coordinates(base_screen['Логин пароль'])
        assert login_and_password
        ss.search_assert_and_log_and_click(base_screen['Имя пользователя'])
        keyboard.write(text['Имя пользователя'])
        ss.search_assert_and_log_and_click(base_screen['Пароль'])
        keyboard.write(text['Пароль'])
        ss.search_assert_and_log_and_click(base_screen['Ок'])
        return ss.search_locate_coordinates(base_screen['Шапка SrvMod'])

    @staticmethod
    def exit_srvmod_cross():
        """Выход из SrvMod крестом"""
        ss.search_assert_and_log_and_click(base_screen['Крестик выхода'])
        return not ss.search_locate_coordinates(base_screen['Шапка SrvMod'], time_search=0)


class ThreeStripes:

    @staticmethod
    def block_and_f12():
        """Три полоски -> Блокировка и F12"""
        ss.search_assert_and_log_and_click(base_screen['Три полоски'])
        general_window = ss.search_locate_coordinates(three_stripes_screen['Три полоски общее окно'])
        assert general_window
        ss.search_assert_and_log_and_click(three_stripes_screen['Блокировка и F12'])
        assert ss.search_locate_coordinates(three_stripes_screen['Требуется подтверждение'])
        ss.search_assert_and_log_and_click(three_stripes_screen['Пароль'])
        keyboard.write(text['Пароль'])
        ss.search_assert_and_log_and_click(three_stripes_screen['Ввод'])
        assert ss.search_locate_coordinates(base_screen['Шапка SrvMod'])
        pg.press('F12')
        ss.search_locate_coordinates(three_stripes_screen['Требуется подтверждение'])
        ss.search_assert_and_log_and_click(three_stripes_screen['Пароль'])
        keyboard.write(text['Пароль'])
        ss.search_assert_and_log_and_click(three_stripes_screen['Ввод'])
        assert ss.search_locate_coordinates(base_screen['Шапка SrvMod'])
        return True

    @staticmethod
    def exit_srvmod_exit():
        """Выход из SrvMod кнопкой выход"""
        three_stripes = ss.search_locate_coordinates(base_screen['Три полоски'])
        assert three_stripes
        pg.click(three_stripes)
        out = ss.search_locate_coordinates(three_stripes_screen['Выход'])
        pg.click(out)
        assert not ss.search_locate_coordinates(base_screen['Шапка SrvMod'], time_search=2)
        return True

    @staticmethod
    def about_the_program():
        """О программе"""
        ss.search_assert_and_log_and_click(base_screen['Три полоски'])
        ss.search_assert_and_log_and_click(three_stripes_screen['О программе'])
        about_win = ss.search_locate_coordinates(three_stripes_screen['О программе окно'])
        assert about_win
        ss.search_assert_and_log_and_click(three_stripes_screen['О программе закрыть'], confidence=0.8)
        return not ss.search_locate_coordinates(three_stripes_screen['О программе окно'], time_search=2)


class Service:

    @staticmethod
    def uploading_authorizations():
        """Выгрузка авторизаций"""
        ss.search_assert_and_log_and_click(base_screen['Сервис'])
        general_window = ss.search_locate_coordinates(service_screen['Сервис общее окно'])
        assert general_window
        ss.search_assert_and_log_and_click(service_screen['Выгрузка авторизаций'])
        login_and_password = ss.search_locate_coordinates(service_screen['Логин пароль'])
        assert login_and_password
        ss.search_assert_and_log_and_click(base_screen['Имя пользователя'])
        keyboard.write(text['Имя пользователя'])
        ss.search_assert_and_log_and_click(base_screen['Пароль'])
        keyboard.write(text['Пароль'])
        ss.search_assert_and_log_and_click(base_screen['Ок'])
        task_complete = ss.search_locate_coordinates(service_screen['Task complete'])
        assert task_complete
        ss.search_assert_and_log_and_click(service_screen['Ok complete'])
        ss.search_assert_and_log_and_click(service_screen['Start'])
        task_complete = ss.search_locate_coordinates(service_screen['Task complete'])
        assert task_complete
        ss.search_assert_and_log_and_click(service_screen['Ok complete'])
        assert ss.search_locate_coordinates(service_screen['Unload authorization'])
        ss.search_assert_and_log_and_click(service_screen['Close'])
        assert not ss.search_locate_coordinates(service_screen['Unload authorization'],
                                                time_search=2)
        return True
