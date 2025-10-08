from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from config.db import collection
from schemas.note import notesEntity
from bson import ObjectId

note = APIRouter()
templates = Jinja2Templates(directory="templates")

# Display all notes
@note.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    notes = notesEntity(collection.find({}))
    return templates.TemplateResponse("index.html", {"request": request, "newNotes": notes})

# Create Note
@note.post("/create", response_class=HTMLResponse)
async def create_note(request: Request):
    form = await request.form()
    title = form.get("title")
    desc = form.get("desc")
    important = bool(form.get("important"))

    if not title or not desc:
        return HTMLResponse("Title and Description cannot be empty.", status_code=400)

    collection.insert_one({
        "title": title,
        "desc": desc,
        "important": important
    })
    return RedirectResponse("/", status_code=303)

# Update Note
@note.post("/update/{note_id}", response_class=HTMLResponse)
async def update_note(request: Request, note_id: str):
    form = await request.form()
    title = form.get("title")
    desc = form.get("desc")
    important = bool(form.get("important"))

    collection.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": {"title": title, "desc": desc, "important": important}}
    )
    return RedirectResponse("/", status_code=303)

# Delete Note
@note.get("/delete/{note_id}")
def delete_note(note_id: str):
    collection.delete_one({"_id": ObjectId(note_id)})
    return RedirectResponse("/", status_code=303)
