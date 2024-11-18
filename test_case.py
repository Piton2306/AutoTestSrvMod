import pyautogui as pg
import pyperclip

import base
from screen_name_and_text import *


def test_authorization():
    base.run_exe_42(base.path_42)
    base.search_locate_coordinates(screen['Логин пароль'])
    login = base.search_locate_coordinates(screen['Имя пользователя'])
    pg.moveTo(login)
    pg.click()
    pyperclip.copy(text['Имя пользователя'])
    pg.hotkey('ctrl', 'v')
    password = base.search_locate_coordinates(screen['Пароль'])
    pg.moveTo(password)
    pg.click()
    pyperclip.copy(text['Пароль'])
    pg.hotkey('ctrl', 'v')
    ok = base.search_locate_coordinates(screen['Ок,окна логина'])
    pg.moveTo(ok)
    pg.click()
