# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1848 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x17\x93u\x88\xd1\xe7vy\xdbQ\xe3`G\x83\x00*\xb0V"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 12
#    module_0.func()