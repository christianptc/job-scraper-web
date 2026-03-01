from pathlib import Path
import sqlite3
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DB_PATH = BASE_DIR / "database.db"

def table_init():
    command = "CREATE TABLE IF NOT EXISTS"

    tablename_jobs = "jobs"
    columns_jobs = (
        "id INTEGER PRIMARY KEY AUTOINCREMENT",
        "company TEXT NOT NULL",
        "position TEXT NOT NULL",
        "link TEXT NOT NULL UNIQUE",
        "date_posted TEXT NOT NULL",
    )
    fields_jobs = ",".join(columns_jobs)


    tablename_users = "users"
    columns_users = (
        "id TEXT NOT NULL PRIMARY KEY",
        f"last_seen TEXT NOT NULL DEFAULT '{datetime.now().strftime('%d.%m.%Y %H:%M')}'",
        "total_time INTEGER NOT NULL DEFAULT 0",
    )
    fields_users = ",".join(columns_users)


    tablename_users_jobs = "user_jobs"
    columns_users_jobs = (
        "userid TEXT NOT NULL",
        "jobid INTEGER NOT NULL",
        "status TEXT NOT NULL DEFAULT 'saved'",
        "last_update TEXT",
        "PRIMARY KEY (userid, jobid)",
        "FOREIGN KEY (userid) REFERENCES users(id)",
        "FOREIGN KEY (jobid) REFERENCES jobs(id)"
    )
    fields_users_jobs = ",".join(columns_users_jobs)


    try:
        with sqlite3.connect(DB_PATH, timeout=20.0) as conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            cur = conn.cursor()
            
            cur.execute(f"{command} {tablename_jobs} ({fields_jobs})")
            cur.execute(f"{command} {tablename_users} ({fields_users})")
            cur.execute(f"{command} {tablename_users_jobs} ({fields_users_jobs})")
        return
    
    except Exception as e:
        print(f"ERROR db_handler/table_init: {e}")
        return
    
