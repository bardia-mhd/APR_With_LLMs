# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import mergesort as module_0
import builtins as module_1


def test_case_0():
    str_0 = "naQ$`^6fX)IVh"
    var_0 = module_0.mergesort(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    module_0.mergesort(object_0)