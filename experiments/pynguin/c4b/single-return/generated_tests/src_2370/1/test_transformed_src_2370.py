# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2370 as module_0


def test_case_0():
    bytes_0 = b"\xeb\x12\xb6*\x12\xbf$w3"
    list_0 = [bytes_0, bytes_0]
    bool_0 = False
    list_1 = [list_0, bool_0, list_0, bool_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "IGNORE HIM!"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "CHAT WITH HER!"