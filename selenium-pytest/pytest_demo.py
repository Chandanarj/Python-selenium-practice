# contents of test_append.py
import pytest

@pytest.fixture
def first_value():
    print("Before Method")    
    yield
    print("After method")
    

def test_assert1(first_value):
    print("TestA")


def test_assert2(first_value):
    print("TestB")
