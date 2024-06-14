filetype = input('enter a filetype? ').strip().lower()

if filetype.endswith('.gif'):
         print('image/gif')
elif filetype.endswith('.png'):
         print('image/png')
elif filetype.endswith('.jpg') | filetype.endswith('.jpeg'):
         print('image/jpeg')         
elif filetype.endswith('.pdf'):
         print('application/pdf') 
elif filetype.endswith('.txt'):
         print('text/plain')        
elif filetype.endswith('.zip'):
         print('application/zip')        
else :
        print('application/octet-stream')              





"""match filetype:
        case 
        case filetype.endswith('.jpg') :
                print('image/jpeg')
        case filetype.endswith('.png'):
                print('image/png')
        case filetype.endswith('.pdf'):
                print('application/pdf')
        case filetype.endswith('.txt'):
                print('text/plain')  
        case filetype.endswith('.zip'):
                print('application/zip')  
        case _: 
                print('application/octet-stream') """                                    


