# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1652 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    int_0 = 207
    bytes_0 = b"\x7f\xf8m\xf7\x7fO`\x1c\xf8wKN\xfcs\x9f3t"
    bool_0 = False
    tuple_0 = (int_0, bytes_0, bool_0)
    var_0 = module_0.func(*tuple_0)