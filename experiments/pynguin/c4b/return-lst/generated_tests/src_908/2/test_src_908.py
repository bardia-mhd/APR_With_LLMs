# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_908 as module_0


def test_case_0():
    str_0 = "}F;\x0cZ\\Q+```B"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "})aF-\x0cqQu{```````na"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
    ]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*list_1)