# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2441 as module_0


def test_case_0():
    bytes_0 = b"\x93\x14]p4\xc9\xde\xf8\x9b\x14]x[Z\x80t\xde"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "nQ"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '"}{^K9qJjU2YOd\x0cb'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "H"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()