# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import pascal as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 581
    var_0 = module_0.pascal(int_0)
    bool_0 = False
    var_1 = module_0.pascal(bool_0)
    int_1 = -152
    var_2 = module_0.pascal(int_1)
    var_3 = module_0.pascal(int_1)
    module_0.pascal(var_1)


def test_case_1():
    bool_0 = True
    var_0 = module_0.pascal(bool_0)