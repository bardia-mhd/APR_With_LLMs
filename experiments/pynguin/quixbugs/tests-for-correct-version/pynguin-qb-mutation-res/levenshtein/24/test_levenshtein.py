# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = 'ay~@y?~lKr"I3bKI<(5f'
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    module_0.levenshtein(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 2371.1
    none_type_0 = None
    module_0.levenshtein(float_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_1.object(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\\b\rx|"
    bytes_0 = b"\xba\x9b\xd5\x03|\x18Lm7_6W\xd2"
    module_0.levenshtein(bytes_0, str_0)