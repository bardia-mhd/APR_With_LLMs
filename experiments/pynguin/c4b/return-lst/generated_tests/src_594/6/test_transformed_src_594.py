# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_594 as module_0


def test_case_0():
    str_0 = "*^\r!D\x0bFO{3"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0]
    var_1 = module_0.func(*list_0)


def test_case_1():
    bytes_0 = b"6h\xb8\xcbE\x13;Mf\xb5`i\x08\xab\xd5{\xcd\xa4"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1111111"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "0000000"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    list_1 = [var_0]
    var_2 = module_0.func(*list_1)
#    module_0.func()