import datetime

#Store the next available id for all the new notes.
last_id=0

class Note:
    '''Representing a note in the notebook.Match against a string in searches
    and store tags for each note'''

    def __init__(self,memo,tags=''):
        '''initialize a note with memo and optional
        space seperated tags.Automatically set the note's
        creation date and a unique id.'''
        self.memo=memo
        self.tags=tags
        self.creation_date=datetime.date.today()
        global last_id
        last_id+=1
        self.id=last_id
    def match(self,filter):
        '''Determine if this note matches the filter text.
        Return True if it matches,False otherwise.

        Search is case sensitive and matches both texts and
        tags.'''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''Represent a collection  of notes that can be tagged
    modified and searched.'''

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes=[]
    def new_note(self,memo,tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo,tags))
    def modify_memo(self,note_id,memo):
        '''Find the note with the given ID and change the
        memo to its given value'''
        note=self._find_note(note_id)
        if note:
            note.memo=memo
            return True
        return False
        
    def modify_tags(self,note_id,tags):
        '''Find the note with the given ID and change the
        tags to the given value'''
        for note in self.notes:
            if note.id==note_id:
                note.tags=tags
                break
    def search(self,filter):
        '''Find all notes memo that match the given filter
        string'''
        return[note 
        for note in self.notes
         if note.match(filter)]

    def _find_note(self,note_id):
        "Locate the note with the given ID"
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
