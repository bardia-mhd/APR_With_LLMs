# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_258 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"\xa5\xb3\x92\x1ej6>\rV\xe1\xd9>\xe0\xbaE\xaft\x81"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa5\xb3\x92\x1e\xbd6>\rV\xd9>\xe0\xbaE\xaft\x81"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa5\xb3\x01\x1ej6>\rV\xd9>\xe0\xbaE\xaft\x81"
    var_0 = module_0.func(*bytes_0)
    str_0 = ""
    list_0 = [str_0, str_0, var_0, bytes_0]
#    module_1.object(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xcc<\x96\xb8\xa8y\xfd\xcb"
    var_0 = module_0.func(*bytes_0)
#    module_1.object(**var_0)