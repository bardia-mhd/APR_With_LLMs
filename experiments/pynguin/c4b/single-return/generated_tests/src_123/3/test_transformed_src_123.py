# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_123 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -3469
    list_0 = [int_0, int_0, int_0, int_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 124
    bool_0 = True
    list_0 = [int_0, bool_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 21008033089631912585034388148024508416
    bool_1 = True
    list_1 = [bool_1, bool_1, bool_1, bool_1]
    var_1 = module_0.func(*list_1)
    assert var_1 == 2
#    module_1.object(*var_1, **var_1)