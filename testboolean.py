def main():
    xx = input('what is CB latest album? ')
    if correctAlbum(xx):
        print('Yes thats correct , go Team Breezy')
    else:
        print('wrong xxx')   
    
def correctAlbum(y):
    if '11:11' in y:
        return True
    else:
        return False

main()



