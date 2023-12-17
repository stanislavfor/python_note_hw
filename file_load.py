
import json

    
def load_notes_from_file():
    try:
        with open("notes_hw/note_files/notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes