# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_908 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ".m4:62]IWYYYYYa\roX3n"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ".m4:62]IYYYYYYY\roX3n"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    var_1 = module_0.func(*list_0)
    assert var_1 == "YES"
#    module_1.object(**var_0)