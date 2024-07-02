from pytest import approx
from pytest import raises
from calc import square

def test2_postive() -> None:
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative() -> None:    
    assert square(-2) == 4
    assert square(-3) == 9

def test_float() -> None:    
    assert square(-2.2) == approx(4.84,abs=0.1)
    # assert isclose(4.84,4.840000, rel_tol=.1)
    
def test_zero() -> None:
    assert square(0) == 0
    
def test_str() -> None:
    with raises(TypeError):
        square('cat')   