import os #used to view, make and list directories
import shutil #used to move files into directories 

main_desktop_path: str = os.path.join(fr'C:\Users\01465307\OneDrive - University of Cape Town','Desktop')    
def ensure_directory_exists(path:str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
        print(f'{path} created')
        
def organize_files_on_desktop() -> None:
    """
    The `organize_files_on_desktop` function organizes files on the desktop based on predefined
    categories and their corresponding file extensions.
    """
    desktop_path:str = os.path.join(os.environ['USERPROFILE'], 'Desktop')    
    # desktop_path = os.path.join(fr'C:\Users\01465307\OneDrive - University of Cape Town','Desktop')    
    
    # List all files on the Desktop
    files:list[str] = os.listdir(desktop_path)
        
    # Define the directory structure as a dictionary,
    # catagory name is the key and the list of extensions represents the values 
    
    dir_structure:dict[str:str] = {
        'PICS': ['.png', '.jpg', '.jpeg'], 
        'DOCS': ['.pdf', '.docx', '.doc', '.txt'],
        'MEDIA': ['.mp4','.wmv','.mkv' ,'.avi', '.mp3', '.flac','.m4a','.aac'],
    }
    
    for file in files:
        
        #gets the path of the current file but joining the desktop path and filename with extension, 
        # as we know we will only be working from the desktop folder
        file_path = os.path.join(desktop_path, file)
        
        # Check if the Path to the file is an actual file 
        if os.path.isfile(file_path):
            
            #seperates the dictionary by catogory and extension 
            for category, extensions in dir_structure.items(): 
                
                #when iterating over each file, we check if its extention matchs that which we have in our list of defined extentions
                if any(file.endswith(ext) for ext in extensions):
                    
                    #if there are any, we create a destination folder using the list of pre-defined catagories 
                    destination_folder = os.path.join(desktop_path, category)
                    
                    #we check if the folder doesnt already exist
                    ensure_directory_exists(destination_folder)
                    
                    #we then use shutil.move() functoin to move the file into the destination folder     
                    # we parse the source which is the file itself, and the destination folder
                    shutil.move(file_path, destination_folder)
                    break
            else:   
                others_folder: str = os.path.join(desktop_path, 'Others')        
                ensure_directory_exists(others_folder)         
                shutil.move(file_path, others_folder)
                

    print("Files organized successfully.")

def organize_docs() -> None:
    #specifying folder paths for the folders we are going to use in this function 
    desktop_path = os.path.join(fr'C:\Users\01465307\OneDrive - University of Cape Town','Desktop')
    docs_path = os.path.join(desktop_path, 'DOCS')
    PDF_folder_path: str = os.path.join(docs_path, 'PDF')
    Word_Docs_path: str = os.path.join(docs_path, 'Word Docs')
    Text_file_path: str = os.path.join(docs_path, 'Text Files')
    Docs_folder: list[str] = os.listdir(docs_path)


    # Mapping file extensions to directories
    file_type_directories:dict[str,str] = {
    PDF_folder_path: '.pdf',
    Word_Docs_path: ('.docx','.doc'),   
    Text_file_path: '.txt',
    }

    for file in Docs_folder:            
        file_path: str = os.path.join(docs_path, file) #get file path of the current file        
        if os.path.isfile(file_path): #ensure path refers to a file and not a directory/folder
            
            for folder, ext in  file_type_directories.items():
                if file.endswith(ext):
                    
                    destination_folder: str = os.path.join(docs_path,folder)
                    ensure_directory_exists(destination_folder)
                    shutil.move(file_path,destination_folder )
                    
if __name__ == "__main__":
    organize_files_on_desktop()
    organize_docs()      
    
    
                  
     
    """Features for another day """               
# def contains_required_files(folder_path:str)-> int:
#     doc_counter: int = 0
#     required_extensions:tuple[str] = (".pdf", ".docx", ".txt",".doc",".xlsx",".csv",)
    
#     for dirpath, dirnames, files in os.walk(folder_path):
#         for file in files:
#             # file_path: str = os.path.join(docs_path, file)
#             if file.endswith(required_extensions) :
#                 doc_counter += 1                
#     return doc_counter

# def path_is_dir() -> None:    
#     #gets a list of the directories on the desktop
#     directories:list[str] = os.listdir(main_desktop_path)  
#     docs_path:str = os.path.join(main_desktop_path, 'DOCS') #gets DOCS folder path
    
#     for folder in directories:
#         folder_path:str = os.path.join(main_desktop_path,folder) #gets path of that folder
        
#         if os.path.isdir(folder_path) and folder_path != docs_path:#checks if the path is actually a folder
#             print(f'{folder} - Folder')
            
#             docs_counter: int = contains_required_files(folder_path)
#             #checks if those folders contains documents 
#             if docs_counter > 0 :
#                 print(f'{docs_counter} in the {folder} folder')
#         else:
#             print(f'{folder} is the DOCS folder') 