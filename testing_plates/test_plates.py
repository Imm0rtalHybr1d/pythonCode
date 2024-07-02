import plates


def test_max_lenth() -> None:
    assert plates.check_max_length('weweewe') == True
    
def test_min_lenth() -> None:
    assert plates.check_min_length('w') == True

def test_first_2() -> None:
    assert plates.check_first_2('12weer') == True

def test_ends_with_letter() -> None:
    assert plates.ends_with_letter('WEWE2W'.lower()) == True

def test_first_num_0() -> None:
    assert plates.first_num_0('CS05'.lower()) == True
    
def test_everything() -> None:
    plate:str = 'wewewe'
    assert (plates.check_max_length(plate),
    plates.check_min_length(plate),
    plates.check_first_2(plate),
    plates.ends_with_letter(plate),
    plates.first_num_0(plate),
    plates.contains_punctuation(plate)) == True

def main():
    ...
 
if __name__ == "__main__":
    main()
 