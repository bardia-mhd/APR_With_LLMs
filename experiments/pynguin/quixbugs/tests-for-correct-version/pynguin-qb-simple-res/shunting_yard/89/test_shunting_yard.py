# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = 'PlS/9:1L0"\\\x0c'
    module_0.shunting_yard(str_0)


def test_case_1():
    str_0 = "q"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"&\xc2\xc48\x89X\xf8\xea\x10\xb7"
    var_0 = module_0.shunting_yard(bytes_0)
    var_1 = module_0.shunting_yard(bytes_0)
    bool_0 = True
    module_0.shunting_yard(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "**`Xw!xu$i=Q7=/`r8"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ","
    var_0 = module_0.shunting_yard(str_0)
    object_0 = module_1.object()
    var_1 = module_0.shunting_yard(var_0)
    str_1 = "-*`Xw!x+$i=Q=/`r8"
    var_2 = module_0.shunting_yard(var_0)
    module_0.shunting_yard(str_1)