# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    int_0 = 860
    none_type_0 = None
    var_0 = module_0.subsequences(none_type_0, none_type_0, bool_0)
    var_1 = module_0.subsequences(bool_0, bool_0, bool_0)
    set_0 = {bool_0, int_0, bool_0, bool_0}
    module_0.subsequences(set_0, var_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    none_type_0 = None
    module_0.subsequences(none_type_0, dict_0, dict_0)


def test_case_2():
    bool_0 = True
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    bool_1 = True
    var_0 = module_0.subsequences(bool_0, bool_1, bool_0)
    int_0 = 124
    var_1 = module_0.subsequences(bool_0, int_0, bool_0)
    bytes_0 = b"\xd2."
    module_0.subsequences(bytes_0, var_0, bool_0)