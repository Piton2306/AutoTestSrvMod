import pytest

from base import LogsTestInfo
from list_to_case import *

lg = LogsTestInfo()
ts = ThreeStripes()
bs = Base()
sr = Service()


class Test1:
    """"Тест входа и выхода из SrvMod"""
    name_test = 'Test1'

    def test_start_authorization_srvmod(self):
        lg.log_start(self.name_test)
        assert bs.start_authorization_srvmod(), lg.logs_error_false(f"{self.name_test} start_authorization_srvmod")
        lg.logs_info_true(f"{self.name_test} start_authorization_srvmod")

    def test_exit_srvmod_exit(self):
        assert ts.exit_srvmod_exit(), lg.logs_error_false(f"{self.name_test} exit_srvmod_exit")
        lg.logs_info_true(f"{self.name_test} exit_srvmod_exit")
        lg.log_finish(self.name_test)


class Test2:
    """Тест блокировки SrvMod """
    name_test = 'Test2'

    def test_start_authorization_srvmod(self):
        lg.log_start(self.name_test)
        assert bs.start_authorization_srvmod(), lg.logs_error_false(f"{self.name_test} start_authorization_srvmod")
        lg.logs_info_true(f"{self.name_test} start_authorization_srvmod")

    @pytest.mark.xfail()
    def test_block_and_f12(self):
        assert ts.block_and_f12(), lg.logs_error_false(f"{self.name_test} block_and_f12")
        lg.logs_info_true(f"{self.name_test} block_and_f12")

    def test_exit_srvmod_exit(self):
        assert ts.exit_srvmod_exit(), lg.logs_error_false(f"{self.name_test} exit_srvmod_exit")
        lg.logs_info_true(f"{self.name_test} exit_srvmod_exit")
        lg.log_finish(self.name_test)


class Test3:
    """Тест 'О программе'"""
    name_test = 'Test3'

    def test_start_authorization_srvmod(self):
        lg.log_start(self.name_test)
        assert bs.start_authorization_srvmod(), lg.logs_error_false(f"{self.name_test} start_authorization_srvmod")
        lg.logs_info_true(f"{self.name_test} start_authorization_srvmod")

    def test_about_the_program(self):
        assert ts.about_the_program(), lg.logs_error_false(f"{self.name_test} about_the_program")
        lg.logs_info_true(f"{self.name_test} about_the_program")

    def test_exit_srvmod_exit(self):
        assert ts.exit_srvmod_exit(), lg.logs_error_false(f"{self.name_test} exit_srvmod_exit")
        lg.logs_info_true(f"{self.name_test} exit_srvmod_exit")
        lg.log_finish(self.name_test)


class Test4:
    name_test = 'Test4'

    def test_start_authorization_srvmod(self):
        lg.log_start(self.name_test)
        assert bs.start_authorization_srvmod(), lg.logs_error_false(f"{self.name_test} start_authorization_srvmod")
        lg.logs_info_true(f"{self.name_test} start_authorization_srvmod")

    def test_uploading_authorizations(self):
        assert sr.uploading_authorizations(), lg.logs_error_false(f"{self.name_test} uploading_authorizations")
        lg.logs_info_true(f"{self.name_test} uploading_authorizations")

    def test_exit_srvmod_exit(self):
        assert ts.exit_srvmod_exit(), lg.logs_error_false(f"{self.name_test} exit_srvmod_exit")
        lg.logs_info_true(f"{self.name_test} exit_srvmod_exit")
        lg.log_finish(self.name_test)
