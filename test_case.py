import pytest

from list_to_case import *

ts = ThreeStripes()
bs = Base()


class Test1:
    """"Тест входа и выхода из SrvMod"""

    def test_start_authorization_srvmod(self):
        assert bs.start_authorization_srvmod()

    def test_exit_srvmod_exit(self):
        assert bs.exit_srvmod_cross()


class Test2:
    """Тест блокировки SrvMod """

    def test_start_authorization_srvmod(self):
        assert bs.start_authorization_srvmod()

    @pytest.mark.xfail()
    def test_block_and_f12(self):
        assert ts.block_and_f12()

    def test_exit_srvmod_cross(self):
        assert ts.exit_srvmod_exit()


class Test3:
    """Тест 'О программе'"""

    def test_start_authorization_srvmod(self):
        assert bs.start_authorization_srvmod()

    def test_about_the_program(self):
        assert ts.about_the_program()

    def test_exit_srvmod_cross(self):
        assert ts.exit_srvmod_exit()
