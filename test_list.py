from base import run_exe_42, path_42
from base import search_locate_coordinates as sc
from screen_name_and_text import *


def test_answer():
    assert run_exe_42(path_42) == 'Ок'


def test_search_screen():
    assert sc(screen['Логин пароль'])
