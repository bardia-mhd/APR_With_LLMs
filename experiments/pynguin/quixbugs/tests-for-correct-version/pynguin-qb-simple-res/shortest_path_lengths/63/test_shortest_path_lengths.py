# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_lengths as module_0
import collections as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.shortest_path_lengths(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.shortest_path_lengths(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    set_0 = set()
    var_0 = module_0.shortest_path_lengths(bool_0, set_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "collections.defaultdict"
    )
    assert len(var_0) == 1
    assert (
        f"{type(module_1.defaultdict.default_factory).__module__}.{type(module_1.defaultdict.default_factory).__qualname__}"
        == "builtins.member_descriptor"
    )
    none_type_0 = None
    module_0.shortest_path_lengths(bool_0, none_type_0)