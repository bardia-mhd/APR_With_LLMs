# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1089 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xea\xd7\xba\xfdD"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa3\x01\xb6\xc9\xe4G\xad\xf4P\xd5\xc8"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES\n-1"
#    module_0.func(*var_0)