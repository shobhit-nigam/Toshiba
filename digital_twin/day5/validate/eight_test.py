import pytest

def test_funca(funcc):
	varx = 10
	vary = 12
	assert funcc[0]==varx, "y test failed"

def test_funcb(funcc):
	varx = 8
	vary = 12
	assert funcc[1]==varx, "y test failed"

@pytest.fixture
def funcc():
	varx = 10
	vary = 12
	return [varx, vary]
