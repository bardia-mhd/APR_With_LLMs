# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_2388 as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = '\t(9`KQdo^hiT"-d#:y"'
    object_0 = module_0.object()
    dict_0 = {str_0: object_0}
    list_0 = [str_0, str_0, str_0, dict_0]
    var_0 = module_1.func(*list_0)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_1.func(*list_0)