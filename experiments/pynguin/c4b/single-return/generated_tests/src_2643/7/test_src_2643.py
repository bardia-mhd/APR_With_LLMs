# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2643 as module_0


def test_case_0():
    str_0 = "MqVyj]Zps2TdtEWA\tE$"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_1():
    str_0 = "qVyp2T!tEW/AEV"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    list_0 = [str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "\x0b!JSK\\@nC}&\t"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_4():
    str_0 = "K/Nu(1R~Mc "
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_5():
    str_0 = "MqVy]Zps2TdtEW/A\tE$V"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_6():
    str_0 = "M.dAEA\tEVV"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_7():
    str_0 = "qVKyp2T!tEW/AEV"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_8():
    str_0 = "Kka_vNJ=KK^V>wplE"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_9():
    str_0 = "K4KKKPVpE"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_10():
    str_0 = "KKP!cVpE"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_11():
    str_0 = "KKKVVPlsg"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_12():
    str_0 = "KKVVVps"
    list_0 = [
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
        str_0,
        str_0,
        str_0,
    ]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1