# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "}./|zipvU7M*\r\nGL"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == -1
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    module_0.find_in_sorted(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "W"
    var_0 = module_0.find_in_sorted(str_0, str_0)
    assert var_0 == 0
    str_1 = "B*x>\nBh7E"
    var_1 = module_0.find_in_sorted(str_1, str_1)
    assert var_1 == -1
    object_0 = module_1.object()
    none_type_0 = None
    module_0.find_in_sorted(object_0, none_type_0)