import pytest

from employee import Employee

@pytest.fixture
def me():
    me = Employee("male", 1_000_000)
    return me

def test_give_default_raise(me):
    me.give_raise()
    assert me.salary == 1_500_000

def test_give_custom_raise(me):
    me.give_raise(1)
    assert me.salary == 1_000_001