# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


def test_case_0():
    bytes_0 = b"-\xe7x\x8b\x12\xb1\xd9\xa2\x04F!\xb2q\x0e\x97\xb1\x95A"
    var_0 = module_0.shunting_yard(bytes_0)


def test_case_1():
    str_0 = "h"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "VM3E)q8A"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "++92p0\tX\x0b}]>\x0c\\\\V%S "
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "}OW[$l[5+W\rfx;i?n`"
    list_0 = [str_0]
    bytes_0 = b"\xf27\xc5FsY\xba&$\xe1\x80C\xe34"
    var_0 = module_0.shunting_yard(bytes_0)
    var_1 = module_0.shunting_yard(list_0)
    str_1 = "+*92Gp0V\tsX\x0b}]\\u%S "
    module_0.shunting_yard(str_1)