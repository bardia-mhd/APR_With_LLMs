# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2357 as module_0


def test_case_0():
    bytes_0 = b"\xb7\xf6\x89f\x8f\xaa\x81Sz\xa86t\xcaJ"
    var_0 = module_0.func(*bytes_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()