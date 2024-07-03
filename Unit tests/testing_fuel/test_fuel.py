import fuel

def test_fraction() ->any:
    assert fuel.get_fraction(2,2) == 'F'

def test_divide() ->any:
    assert fuel.divid_by_0(2,0) == f'Cannot divide by Zero >>> division by zero'
    
def test_convert() ->any:
    assert fuel.split_convert('2/2') == (2,2)
