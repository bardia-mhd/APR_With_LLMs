# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1770 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    str_0 = "-P,y@0#]"
    list_0 = [bool_0, str_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"^\x0fn\xe5zU\xed-MTG\xdc\x99\xd1\x1d\xaf"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 19565255464643158563444752384
    float_0 = -1499.106
#    module_0.func(*float_0)