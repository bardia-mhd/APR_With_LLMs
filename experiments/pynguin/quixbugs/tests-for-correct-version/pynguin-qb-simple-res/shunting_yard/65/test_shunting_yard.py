# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


def test_case_0():
    bytes_0 = b"8\xdfh?\xcf"
    var_0 = module_0.shunting_yard(bytes_0)


def test_case_1():
    str_0 = "l"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -477
    module_0.shunting_yard(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "g95Ba 1EF1[V)YG"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "/+C!r\nK\t`1JQb"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    list_0 = []
    var_0 = module_0.shunting_yard(list_0)
    str_0 = "+*!r\nK.\t1JQb"
    module_0.shunting_yard(str_0)