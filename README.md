## 📝 iNotes — Makes Task Easy!

iNotes is a modern, responsive task management web app built with **FastAPI** and **Bootstrap 5**. It allows users to create, edit, and delete notes with a clean UI, toast notifications, and confetti animations for delightful feedback.

---

### 🚀 Features

- ✅ Add, edit, delete notes
- 📌 Mark notes as important
- 🎨 Responsive UI with Bootstrap 5
- ✨ Toast + confetti animation on note creation
- 📭 Empty state illustration with motivational quote
- 🧠 Modal-based editing for seamless updates

---

### 🛠️ Tech Stack

| Layer       | Technology           |
|-------------|----------------------|
| Frontend    | HTML, Bootstrap 5, Font Awesome |
| Backend     | FastAPI              |
| Templating  | Jinja2               |
| Database    | MongoDB |

---

### 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/techmuskan/inotes.git
   cd inotes
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

5. **Visit the app**
   ```
   http://127.0.0.1:8000
   ```

---

### 📁 Project Structure

```
inotes-fastapi/
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css
├── models.py
├── main.py
├── database.py
├── requirements.txt
└── README.md
```

---

### 📜 Sample FastAPI Routes

```python
@app.get("/", response_class=HTMLResponse)
def read_notes(request: Request):
    # Fetch notes from DB and render template
    return templates.TemplateResponse("index.html", {"request": request, "newNotes": notes})

@app.post("/create")
def create_note(...):
    # Add note to DB

@app.post("/update/{note_id}")
def update_note(...):
    # Update note in DB

@app.get("/delete/{note_id}")
def delete_note(...):
    # Delete note from DB
```

---

### 💡 Future Enhancements

- 🔍 Search and filter notes
- 🌙 Dark mode toggle
- 📅 Due dates and reminders
- 🗂️ Categories and tags

---

### 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to improve.

---
