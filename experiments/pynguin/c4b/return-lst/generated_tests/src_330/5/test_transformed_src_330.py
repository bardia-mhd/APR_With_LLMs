# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_330 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    bytes_0 = b"K\x1f\xfd\x9c\x80\x90\xf5\xea\x95"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()