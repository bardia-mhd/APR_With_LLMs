# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_522 as module_0


def test_case_0():
    bytes_0 = b"\xb6\xa1\x963\x82\xb9\xd9E\xcfJ"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    var_3 = module_0.func(*var_2)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 3305
#    module_0.func(*int_0)


def test_case_2():
    bytes_0 = b"\xb6\xa1\x963\x82\xb9\xd9E\xcfJ"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"Pyn\xa5\xa6\x1b\x07\xfb:'\xe9\x94\xcc"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()