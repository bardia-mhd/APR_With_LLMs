# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    bool_1 = True
    var_0 = module_0.subsequences(bool_0, bool_1, bool_1)
    bool_2 = False
    var_1 = module_0.subsequences(bool_2, bool_0, bool_0)
    module_0.subsequences(bool_0, var_1, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x18\xe9%>\xaf\x16=\x1b\xea\xcb\x10=\x84\xf9\xb3O"
    module_0.subsequences(bytes_0, bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)
    module_0.subsequences(var_0, bool_0, bool_0)