import pytest
from max import Max

@pytest.fixture
def max():
    return Max()

# Data-Driven Testing
def assert_test(test_func):
    cases = [{ 'input': None, 'expect': 0 }, { 'input': [], 'expect': 0 }, { 'input': [3], 'expect': 3 }, { 'input': [2, 1, 3], 'expect': 3 }]
    for case in cases:
        assert test_func(case['input']) == case['expect']

def test_max(max):
    assert_test(max.max)

def test_maxRecursive(max):
    assert_test(max.maxRecursive)