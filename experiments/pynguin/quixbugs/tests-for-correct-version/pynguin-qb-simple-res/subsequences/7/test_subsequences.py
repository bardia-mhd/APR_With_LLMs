# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "8J0AA.Ni]`=/"
    module_0.subsequences(str_0, str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1248
    var_0 = module_0.subsequences(int_0, int_0, int_0)
    bool_0 = False
    var_1 = module_0.subsequences(bool_0, bool_0, bool_0)
    var_2 = module_0.subsequences(bool_0, bool_0, int_0)
    bool_1 = True
    var_3 = module_0.subsequences(bool_0, bool_1, bool_1)
    module_0.subsequences(var_1, bool_0, var_1)