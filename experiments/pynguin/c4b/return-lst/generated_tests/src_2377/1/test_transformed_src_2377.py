# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2377 as module_0


def test_case_0():
    str_0 = "R"
    var_0 = module_0.func(*str_0)


def test_case_1():
    str_0 = "Bzb\\q@_}h\nuy^_let09"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    str_0 = "Bzb\\q@._}h\nue^_let09"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "B%9@:_p}hqe{0_le0l"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "B%9@:_p}hqe{0_le0lz"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "B%9@:_phqe{_le0lxo"
    list_0 = [str_0]
#    module_0.func(*list_0)