# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import hanoi as module_0


def test_case_0():
    bool_0 = True
    var_0 = module_0.hanoi(bool_0)
    bool_1 = False
    bytes_0 = b"\xf0\xb4\xbew\xa8~\x9aj\x93\xd7\x1c\xd1]\x98\n\x0co\xf9\x8d"
    var_1 = module_0.hanoi(bool_1, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1982
    none_type_0 = None
    var_0 = module_0.hanoi(int_0, end=none_type_0)
    module_0.hanoi(var_0, none_type_0, int_0)