# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_799 as module_0


def test_case_0():
    bytes_0 = b"\x97\xffY\xfd\xae}o\x8c\xfb&J\xeeFo\xc5\xe2~\x9a\xe6\xfe"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    list_0 = []
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)


def test_case_3():
    str_0 = "4"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "4"
    list_0 = [str_0, str_0, str_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "7"
    tuple_0 = (str_0, str_0)
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()