# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1169 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"E\x0e\xec\xdfN\xb4\x04\xb7\xc6K\xe2\xb0\xd1Q"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 54809
#    module_0.func()


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()