# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2115 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "\n)"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xf7\xf1ULe\x83\x88\x0c\x9914\x89\x8a\x18\xf4\xc8'=\x94m"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, list_0, list_0, var_0]
    object_0 = module_0.func(*list_1)
    object_1 = module_1.object()
#    module_0.func()