# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_196 as module_0


def test_case_0():
    str_0 = "!"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "yN8qScatu~r7z-\x0bqN(OF"
    list_0 = [str_0]
    object_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "6\"=i+5Xn!YRmDg%'/\x0bh"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "R-!M;V=|Xp$\nzxi+"
    list_0 = [str_0, str_0, str_0]
    module_0.func(*list_0)