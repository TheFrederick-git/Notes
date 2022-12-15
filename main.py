"""Hlavní soubor aplikace"""

from flask import Flask, render_template, redirect, request, Response
from control import get_notes, add_note, remove_note

app = Flask(__name__, template_folder="./templates", static_folder="./static")

@app.route("/")
def index() -> str:
    """Oteveře domovskou stránku"""

    return render_template("index.html", rows=get_notes())

@app.route("/new")
def create_note() -> str:
    """Otevře stránku pro tvorbu poznámky"""

    return render_template("new.html")

@app.route("/show/<int:note_id>")
def show_note(note_id: str) -> str:
    """Otevře poznámku"""

    return render_template("show.html", row=get_notes(True, note_id))

@app.route("/add", methods = ['POST'])
def db_add() -> Response:
    """Post metoda určena pro zápis do databáze"""

    add_note(request.form["name"], request.form["text"])
    return redirect("/")

@app.route("/remove/<int:note_id>")
def db_remove(note_id: str) -> Response:
    """Post metoda určena pro odstranění dat z databáze"""

    remove_note(note_id)
    return redirect("/")

@app.errorhandler(Exception)
def show_error(code: str) -> str:
    """Vrátí stránku s kočičím obrázkem chyby"""

    return render_template("error.html", code=str(code)[:3])

if __name__ == "__main__":
    app.run()
