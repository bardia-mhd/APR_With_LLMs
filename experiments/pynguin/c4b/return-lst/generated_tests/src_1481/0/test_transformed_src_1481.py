# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1481 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b";B\xaf6D2"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
    var_1 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xf1\x0c;B\xaf6D2"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
    var_1 = module_0.func(*bytes_0)
#    module_0.func()