import pytest

@pytest.fixture
def test_data_setup():
    print("Before Method")
    yield
    print("After Method")

@pytest.fixture
def test_data():
    return [10, 20]


def test_A(test_data_setup, test_data):
    print(test_data)
    print("Method A")


def test_B(test_data_setup):
    print("Method B")