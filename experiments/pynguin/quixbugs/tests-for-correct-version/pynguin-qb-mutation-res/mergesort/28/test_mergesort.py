# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import mergesort as module_0


def test_case_0():
    bytes_0 = b""
    var_0 = module_0.mergesort(bytes_0)
    assert var_0 == b""


def test_case_1():
    bytes_0 = b"\x93xF&\xba\xbe\xc8\x95SXEA\x1eh\xaeL\x0f"
    var_0 = module_0.mergesort(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.mergesort(bool_0)