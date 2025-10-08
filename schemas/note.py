from bson import ObjectId

def noteEntity(note) -> dict:
    return {
        "id": str(note["_id"]),
        "title": note.get("title", "(no title)"),
        "desc": note.get("desc", "(empty)"),
        "important": note.get("important", False)
    }

def notesEntity(notes) -> list:
    return [noteEntity(n) for n in notes]
