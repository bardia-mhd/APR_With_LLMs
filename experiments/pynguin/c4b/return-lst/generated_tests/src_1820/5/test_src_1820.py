# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1820 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xfc\xc2\xb7\x9eqG\x0f\xf4\xf8\xa4q\xf5c\xeab\x98\xbc\xd3"
    var_0 = module_0.func(*bytes_0)
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"M\xbe\x14w\xaa"
    var_0 = module_0.func(*bytes_0)
    module_0.func()