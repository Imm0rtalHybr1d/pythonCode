userAns = input("What the Great Question of Life, the Universe and Everything? ").lower()

match userAns:
        case '42' | 'forty-two' | 'forty two':
                print('Yes')
        case _: 
                print('No')        