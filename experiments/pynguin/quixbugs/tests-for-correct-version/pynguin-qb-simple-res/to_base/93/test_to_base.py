# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0
import re as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 178
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    var_1 = module_0.to_base(int_0, int_0)
    assert var_1 == "10"
    none_type_0 = None
    module_0.to_base(var_1, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -4405
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == ""
    int_1 = 1796
    none_type_0 = None
    module_1.compile(int_1, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)