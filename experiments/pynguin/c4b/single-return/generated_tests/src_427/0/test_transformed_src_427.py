# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_427 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "9:9Toj'vXa\n"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 11


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ',?"b=k>UMSk4G>F'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8
#    module_0.func()