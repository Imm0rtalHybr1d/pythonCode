from dataclasses import dataclass, field
from uuid import uuid4, UUID # used to create unique ID for our notes, notes can have the same name/ content but will be unique cause of the uuid


@dataclass
class Note:
    id: UUID = field(init=False) #runs with __post_init__
    title: str
    body: str
    
    def __post_init__(self):
        self.id = uuid4()

class NoteApp:
    #initializer take Author and optionally a list of notes (set to none by default)
    def __init__(self, author:str, notes:list[Note]| None = None) -> None:
        self.author = author
        
        #if no notes provided then create an empty list of notes else use the list of notes provided by user
        if notes is None:
            self.notes = []
        else:
            self._notes = notes #_notes specify that notes variable only to be used within class

        self.display_instructions()
    
    @staticmethod #not dependant on the instance, purely to display instrctions 
    def display_instructions() -> None:
        print('Welcome to Notes!')
        print('Here are the commands:')
        print('1 - Add new note')
        print('2 - Edit note')
        print('3 - Delete note')
        print('4 - Display all notes')
    
    def _addnote(self) -> None: #_addnote only used inside the class
        title: str = input('Title: ')
        body: str = input('Body:')    
        
        note: Note = Note(title, body) #creating a note 
        self._notes.append(note) #
        print('Note was added!')
        
    def _editnote(self) -> None:
        print('Which note would you like to edit')
        self._show_notes()
        
        try:# we use minus one because for the user the index starts at 1 
            #but in our program a list index starts at 0
            note_index: int = int(input('Index: ')) - 1 
            current_note: Note = self._notes[note_index]
            
            new_title: str = input('Title: ')
            new_body: str = input('Body: ')
            
            current_note.title = new_title
            current_note.body = new_body
            print('Note was updated')
        except IndexError:
            print('Please select a valid note')
            self._editnote() #recursion, takes user to the top of this function to edit note
        except ValueError:
            print('Index cannot be empty')
            self._editnote()
    
    def _delete_note(self) -> None:
        print('Which note would you like to delete')
        self._show_notes()
        
        try:
            note_index: int = int(input('Index: ')) - 1
            del self._notes[note_index]
            print('Note was deleted')
        except IndexError:
            print('Please select a valid note')
            self._delete_note() #recursion, takes user to the top of this function to edit note
        except ValueError:
            print('Index cannot be empty')
            self._delete_note()
    
        
    def _show_notes(self) -> None:
        if not self.notes: 
            print('No notes')
        
            
       
    
    
def main():
    NoteApp.display_instructions()
    
    
 
if __name__ == "__main__":
    main()
         
        
    
