import pytest

@pytest.mark.xfail
def test_example():
    print("DOES NOT GET PRINTED")
    assert 1 == 1


def test_example1():
    assert 1 == 1