# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0
import builtins as module_1


def test_case_0():
    str_0 = " "
    object_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"R\xc9\xcd\x07\xecD73\xbc\x92\x85\xfb\x0f"
    var_0 = module_0.shunting_yard(bytes_0)
    set_0 = set()
    tuple_0 = (var_0, var_0, set_0, var_0)
    module_0.shunting_yard(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "+*2`\riTyJC_ij"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "+*/\rioyJC_j"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x97\xbek<\xef"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    var_0 = module_0.shunting_yard(dict_0)
    var_1 = module_0.shunting_yard(bytes_0)
    var_2 = module_0.shunting_yard(dict_0)
    var_3 = module_0.shunting_yard(var_0)
    object_0 = module_1.object()
    var_4 = module_1.object()
    str_0 = "+*/-io\\yJC_j"
    module_0.shunting_yard(str_0)