# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "nKwcS!W5o)bh:\x0b"
    module_0.shunting_yard(str_0)


def test_case_1():
    str_0 = "`"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x9dTrZ\x18\xda\x0b\x93\x03\xdaY?_L&\xba\x19"
    var_0 = module_0.shunting_yard(bytes_0)
    str_0 = "//u\t,2CO;N"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    module_0.shunting_yard(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "//u\t,2CO;N"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "+//u\t,2CO;N"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "+//+\tC2CO;N"
    module_0.shunting_yard(str_0)