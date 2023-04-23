"""Soubor funkcí pro práci s databází"""

from sqlite3 import connect, Row
from datetime import datetime

PATH: str = "./notes.db"

def init_db() -> None:
    """Vytvoří databázi pro ukládání poznámek"""

    conn = connect("./notes.db")
    conn.cursor().execute("""
    CREATE TABLE IF NOT EXISTS "Notes" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL DEFAULT 'None',
	"Text"	TEXT NOT NULL DEFAULT 'None',
	"Date"	TEXT NOT NULL,
	PRIMARY KEY("ID")
    )
    """)
    conn.commit()
    conn.close()

def get_notes() -> list[dict[str,str]]:
    """Vrátí veškeré uložené poznámky"""

    con = connect(PATH)
    con.row_factory = Row
    cursor = con.cursor()
    data = cursor.execute("SELECT * FROM Notes").fetchall()
    con.commit()
    con.close()
    return data

def get_note(note_id:str) -> tuple[str]|None:
    """Vrátí konkrétní poznámku na základě ID"""

    con = connect(PATH)
    con.row_factory = Row
    cursor = con.cursor()
    data = cursor.execute("SELECT * FROM Notes WHERE ID=?", (note_id,)).fetchone()
    con.commit()
    con.close()
    return data if data else None

def add_note(name:str, text:str) -> None:
    """Přidá poznámku do databáze"""

    con = connect(PATH)
    cursor = con.cursor()
    cursor.execute("INSERT INTO Notes (Name, Text, Date) VALUES (?, ?, ?)",
    (name, text.replace("\n","<br>"), str(datetime.today())[:-7]))
    con.commit()
    con.close()

def remove_note(note_id:str) -> None:
    """Smaže poznámku z databáze"""

    con = connect(PATH)
    cursor = con.cursor()
    cursor.execute("DELETE FROM Notes WHERE ID=?", (note_id,))
    con.commit()
    con.close()
