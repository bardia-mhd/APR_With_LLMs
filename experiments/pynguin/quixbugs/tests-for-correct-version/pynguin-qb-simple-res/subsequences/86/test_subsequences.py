# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    none_type_0 = None
    var_0 = module_0.subsequences(dict_0, none_type_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b":\x8b\xa3\x9a\xe8^b9"
    module_0.subsequences(bytes_0, bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    bool_1 = True
    var_0 = module_0.subsequences(bool_0, bool_1, bool_1)
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    none_type_0 = None
    var_1 = module_0.subsequences(dict_0, none_type_0, bool_0)
    module_0.subsequences(none_type_0, none_type_0, var_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)
    int_0 = -2575
    object_0 = module_1.object()
    module_0.subsequences(object_0, object_0, int_0)