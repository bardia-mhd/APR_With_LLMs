# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_523 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    var_0 = module_0.func(*set_0)
    object_0 = module_1.object()
#    module_0.func(*object_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b"\x02\x00\x9e\x1a\xb3"
    var_0 = module_0.func(*bytes_0)


def test_case_3():
    bool_0 = False
    set_0 = {bool_0, bool_0}
    var_0 = module_0.func(*set_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 2237
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()