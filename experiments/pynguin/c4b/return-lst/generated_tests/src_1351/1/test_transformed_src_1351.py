# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1351 as module_0


def test_case_0():
    str_0 = "^'y:0zEE3"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ".d0$iVJ]"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"UFJC\x1e\xb58"
    list_1 = [bytes_0]
    list_2 = [list_1, list_1, bytes_0, bytes_0]
#    module_0.func(*list_2)