# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_14 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -2867
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"P\xc9H\r\x93\xb4G\xd7\xbc\x8a\xef\xf6\xf8\xdf\\h\xa0\x80\x84\x11"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
#    module_0.func()