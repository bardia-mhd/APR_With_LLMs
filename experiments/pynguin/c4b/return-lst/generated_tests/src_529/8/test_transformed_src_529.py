# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_529 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xcbl\xae\x10E\xd3\x8e\xfc\xf5\xf9mtX1d\xfeF\x97\xf5"
    set_0 = {bytes_0, bytes_0, bytes_0}
    var_0 = module_0.func(*set_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xcbl\xae\x10E\xd3\x8e\xfc\xf5\xf9(tX1d\xfeF\x97\xf5"
    set_0 = {bytes_0, bytes_0, bytes_0}
    list_0 = [set_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0]
    list_2 = [list_1, list_0]
    var_0 = module_0.func(*list_2)
    var_1 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0, list_0, list_0, list_0, list_0, list_0]
    list_2 = [list_1, list_0]
    var_0 = module_0.func(*list_2)
    var_1 = module_0.func(*list_1)
#    module_1.object(*var_1)