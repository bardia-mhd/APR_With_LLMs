# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0
import re as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1784
    none_type_0 = None
    module_0.to_base(int_0, none_type_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.to_base(bool_0, bool_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1660
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    none_type_0 = None
    module_1.escape(none_type_0)