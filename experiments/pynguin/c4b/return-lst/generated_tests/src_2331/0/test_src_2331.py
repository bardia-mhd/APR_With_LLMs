# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2331 as module_0


def test_case_0():
    str_0 = "uG@<Md(\t"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "9kD+3q$5rmUir0*a"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "QG@*Md(Q"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "BiHX~o~3Q6~_"
    bool_0 = True
    list_0 = [str_0, str_0, str_0, bool_0]
    module_0.func(*list_0)