# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import pascal as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 263
    var_0 = module_0.pascal(int_0)
    bool_0 = False
    var_1 = module_0.pascal(bool_0)
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    str_0 = "$]0~'T\tR&y#_"
    str_1 = ")Q<$]%FnlY&+%"
    var_2 = module_0.pascal(bool_0)
    dict_0 = {str_0: none_type_0, str_1: none_type_0, str_1: none_type_0}
    module_1.object(*list_0, **dict_0)


def test_case_1():
    bool_0 = True
    var_0 = module_0.pascal(bool_0)
    var_1 = module_0.pascal(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.pascal(none_type_0)