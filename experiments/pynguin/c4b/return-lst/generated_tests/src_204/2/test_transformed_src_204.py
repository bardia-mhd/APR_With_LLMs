# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_204 as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    object_0 = module_0.object()
    var_0 = module_1.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 926
    list_0 = [int_0]
    var_0 = module_1.func(*list_0)
#    module_1.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_1.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xb7[\xfd0\x9f\x93\xe8a^i\x8e\x9f\xbf\x92-\xfe\xb0\x97"
    var_0 = module_1.func(*bytes_0)
#    module_1.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xc1\xf8\xaa\xac\x8fB\x08PGE)\x15`"
    var_0 = module_1.func(*bytes_0)
#    module_1.func()