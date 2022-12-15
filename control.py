"""Soubor funkcí pro práci s databází"""

from sqlite3 import connect, Row
from typing import Any
from datetime import datetime

PATH = "./notes.db"

def get_notes(one: bool=False, *note_id: str) -> Any:
    """Vrátí veškeré uložené poznámky"""

    con = connect(PATH)
    con.row_factory = Row
    cursor = con.cursor()
    if one:
        data = cursor.execute("SELECT * FROM Notes WHERE ID=?;", (note_id)).fetchone()
    else:
        data = cursor.execute("SELECT * FROM Notes;").fetchall()
    con.commit()
    con.close()
    return data

def add_note(name: str, text: str) -> None:
    """Přidá poznámku do databáze"""

    con = connect(PATH)
    cursor = con.cursor()
    cursor.execute("INSERT INTO Notes (Name, Text, Date) VALUES (?, ?, ?);",
    (name, text.replace("\n","<br>"), str(datetime.today())[:-7]))
    con.commit()
    con.close()

def remove_note(note_id: str) -> None:
    """Smaže poznámku z databáze"""

    con = connect(PATH)
    cursor = con.cursor()
    cursor.execute("DELETE FROM Notes WHERE ID=?;", (str(note_id)))
    con.commit()
    con.close()
