import pytest

def test_funca():
	varx = 10
	vary = 12
	assert varx+2 == vary, "y test failed"
	assert vary == varx, "x test failed"

def test_method():
	varx = 10
	vary = 12
	assert varx+4 == vary, "y test failed"

@pytest.mark.highpri
def test_code():
	varx = 10
	vary = 12
	assert varx+4 == vary, "y test failed"
