# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    bool_0 = True
    bool_1 = False
    var_0 = module_0.subsequences(bool_1, bool_1, bool_1)
    var_1 = module_0.subsequences(bool_1, bool_0, bool_0)
    list_0 = [bool_1, bool_0, dict_0]
    module_0.subsequences(list_0, list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.subsequences(dict_0, dict_0, dict_0)


def test_case_2():
    bool_0 = True
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)