# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "YK-f)8U5D;qCK]JVpo"
    module_0.shunting_yard(str_0)


def test_case_1():
    str_0 = "s"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "}?nD"
    bytes_0 = b"\xb6I\xc3>25[\xb6\x98,\x9a\xcb\xfa%"
    var_0 = module_0.shunting_yard(bytes_0)
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.shunting_yard(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "+/WU);Mmm;8X"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "--s!\x0cD"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "-/-#4rqn`=*9"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b"2\x96\xc4\xd5t\xa1u\xccN\x8f\xb1\xeaF\x08\x9bj(\x02\x9a\x19"
    var_0 = module_0.shunting_yard(bytes_0)
    str_0 = "-//-#4rqn`=*9"
    module_0.shunting_yard(str_0)