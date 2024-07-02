import twttr
import pytest

def shorten(word='testings'):
    assert twttr.loop_through(word) == 'tstngs'
    return twttr.loop_through(word)

def main():    
    print(shorten('testings'))
    
if __name__ == "__main__":
    main()