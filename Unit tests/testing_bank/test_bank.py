import bank


def test_0()->None:
    assert bank.value('hello') == 0
    
def test_20()->None:
    assert bank.value('h')  == 20    

def test_100()->None:
    assert bank.value('ello')  == 100       
    
def main():
    print(test_0())
    print(test_20())
    print(test_100())
    
if __name__ == "__main__":
    main()