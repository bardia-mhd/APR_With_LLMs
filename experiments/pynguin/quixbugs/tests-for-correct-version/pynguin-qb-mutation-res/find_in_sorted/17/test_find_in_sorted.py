# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_in_sorted as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    bytes_0 = b"\x8a\xd8M\xeba\xd0\xbc\x1b!\xa0\x15"
    var_0 = module_0.find_in_sorted(dict_0, bytes_0)
    assert var_0 == -1
    var_1 = module_0.find_in_sorted(dict_0, dict_0)
    assert var_1 == -1
    module_0.find_in_sorted(var_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    list_0 = [object_0, object_0, object_0, object_0]
    module_0.find_in_sorted(list_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_in_sorted(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "PS#"
    str_1 = " [>\x0b-%"
    var_0 = module_0.find_in_sorted(str_1, str_1)
    assert var_0 == -1
    list_0 = []
    object_0 = module_1.object(*list_0)
    module_0.find_in_sorted(str_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "lvRoybf!~d]qs;K\nZ"
    set_0 = {str_0, str_0}
    list_0 = [set_0, str_0, str_0]
    var_0 = module_0.find_in_sorted(list_0, str_0)
    assert var_0 == 1
    dict_0 = {str_0: str_0}
    module_1.object(**dict_0)