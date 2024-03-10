from app import add, sub

# test case for addition function
def test_add():
    assert 6 == add(3,3)


def test_sub():
    assert 2 == sub(4,2)