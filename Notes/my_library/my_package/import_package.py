from my_library import my_package
import sys
import time


if len(sys.argv[1]) == 2:
    time.sleep(3)
    my_package.connect()
    time.sleep(3)
    
    
    my_package.load(sys.argv[1])