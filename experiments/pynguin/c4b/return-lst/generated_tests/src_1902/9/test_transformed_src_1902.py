# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1902 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"+\xa9G\x9f0\x0e\x0c\xcb\x93>\x90#i#v\xae*\xa1"
    var_0 = module_0.func(*bytes_0)
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_1 = module_0.func(*list_0)
    object_0 = module_1.object()
    var_2 = module_1.object()
#    module_0.func()