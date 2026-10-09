import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "projectpulse.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS decisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            decision TEXT NOT NULL,
            reason TEXT NOT NULL,
            constraint_text TEXT NOT NULL,
            person TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            status TEXT NOT NULL DEFAULT 'CURRENT',
            supersedes_id INTEGER,
            FOREIGN KEY (supersedes_id) REFERENCES decisions(id)
        )
    """)

    conn.commit()
    conn.close()
