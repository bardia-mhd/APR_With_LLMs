# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0
import re as module_1
import string as module_2


def test_case_0():
    bool_0 = False
    var_0 = module_0.to_base(bool_0, bool_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_1():
    var_0 = module_1.purge()
    var_1 = var_0.__bool__()
    template_0 = module_2.Template(var_0)
    var_2 = module_0.to_base(var_1, var_1)
    assert var_2 == ""
    var_3 = var_1.__eq__(var_1)
    module_0.to_base(var_3, var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 261
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    none_type_0 = None
    module_0.to_base(none_type_0, int_0)