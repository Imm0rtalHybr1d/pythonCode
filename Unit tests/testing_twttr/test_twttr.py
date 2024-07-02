import twttr

def test(word='testings'):
    assert twttr.loop_through(word) == 'tstngs',f'did not remove all the vowels'
    
    
def main():    
    print(test())
    
if __name__ == "__main__":
    main()