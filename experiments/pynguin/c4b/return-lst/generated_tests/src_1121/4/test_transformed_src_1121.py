# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1121 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "4LC,_Aok"
    var_0 = module_0.func(*str_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xa2\x93\x18\xe8\xc8j\x96\x94\xee~@\xd3\xee\xa6\xff"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xe6@\x0fr&yB\x98\xa7\x15\x97\xc3\xf0"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    bytes_1 = b"\xa2\r\x93\x18\xe8\xc8\xfe\x81\x96\x94\xee\x91~@\xd3\xee\xa6\xff"
    var_2 = module_0.func(*bytes_1)
#    module_0.func()