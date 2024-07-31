import os
import shutil


def organize_files_on_desktop():
    desktop_path:str = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    
    # desktop_path = os.path.join(fr'C:\Users\01465307\OneDrive - University of Cape Town','Desktop') - this is the path of my desktop
    
    # List all files on the Desktop
    files:list[str] = os.listdir(desktop_path)
    
        
    # Define the directory structure as a dictionary,
    # folder name is the key and the list of extensions represents the values 
    
    dir_structure:dict[str:str] = {
        'images': ['.png', '.jpg', '.jpeg'], 
        'DOCS': ['.pdf', '.docx', '.doc', '.txt'],
        'videos': ['.mp4', '.avi'],
    }
    
    #for each file in the list of files 
    for file in files:
        
        #gets the path of the current file but joining the desktop path and the path of that file, as we know we will only be working from the desktop folder
        file_path = os.path.join(desktop_path, file)
        
        # Check if the Path is an actual file 
        # Before attempting to organize the file, it checks if the constructed path points to an existing file using os.path.isfile(file_path). 
        # This step ensures that directories and other non-file items are ignored.
        if os.path.isfile(file_path):
            
            #seperates the dictionary by catogory and extension 
            for category, extensions in dir_structure.items(): 
                
                #when iterating over each file, we check if its extention matchs that which we have in our list of defined extentions
                if any(file.endswith(ext) for ext in extensions):
                    
                    #if there are any, we create a destination folder using the list of pre-defined catagories 
                    destination_folder = os.path.join(desktop_path, category)
                    
                    #we check if the folder doesnt already exist
                    if not os.path.exists(destination_folder):
                        
                        #if if the category folder doesnt exisist, then we use os.makedir to create that catagory folder
                        os.makedirs(destination_folder)
                    
                    #we then use shutil.move() functoin to move the file into the destination folder     
                    # we parse the source which is the file itself, and the destination folder
                    shutil.move(file_path, destination_folder)
                    break
            

    print("Files organized successfully.")

if __name__ == "__main__":
    organize_files_on_desktop()
