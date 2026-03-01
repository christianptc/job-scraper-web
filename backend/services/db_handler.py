from pathlib import Path
import sqlite3
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DB_PATH = BASE_DIR / "database.db"

class handler:
    def __init__(self):
        self.tablename_jobs = "jobs"
        self.tablename_users = "users"
        self.tablename_users_jobs = "user_jobs"
    def table_init(self):
        command = "CREATE TABLE IF NOT EXISTS"

        columns_jobs = (
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "company TEXT NOT NULL",
            "position TEXT NOT NULL",
            "location TEXT NOT NULL",
            "link TEXT NOT NULL UNIQUE",
            "date_posted TEXT NOT NULL",
        )
        fields_jobs = ",".join(columns_jobs)

        columns_users = (
            "id TEXT NOT NULL PRIMARY KEY",
            f"last_seen TEXT NOT NULL DEFAULT '{datetime.now().strftime('%d.%m.%Y %H:%M')}'",
            "total_time INTEGER NOT NULL DEFAULT 0",
        )
        fields_users = ",".join(columns_users)


        columns_users_jobs = (
            "userid TEXT NOT NULL",
            "jobid INTEGER NOT NULL",
            "status TEXT", # when added to favorites, status will get added and i'll just get * from jobid where user == .. and status != NULL
            "last_update TEXT", # upon adding to favorites last_update will get added.
            "PRIMARY KEY (userid, jobid)",
            "FOREIGN KEY (userid) REFERENCES users(id)",
            "FOREIGN KEY (jobid) REFERENCES jobs(id)"
        )
        fields_users_jobs = ",".join(columns_users_jobs)


        try:
            with sqlite3.connect(DB_PATH, timeout=20.0) as conn:
                conn.execute("PRAGMA journal_mode=WAL;")

                cur = conn.cursor()

                cur.execute(f"{command} {self.tablename_jobs} ({fields_jobs})")
                cur.execute(f"{command} {self.tablename_users} ({fields_users})")
                cur.execute(f"{command} {self.tablename_users_jobs} ({fields_users_jobs})")
            return

        except Exception as e:
            print(f"ERROR db_handler/table_init: {e}")
            return


    def get_stored_jobIDs(self, user_id, table):
        valid_tables = ["searched", "favorites"]
        query = f"SELECT jobid FROM {self.tablename_users_jobs} WHERE userid=? AND status IS NULL"

        if table not in valid_tables:
            return []
        
        if table == valid_tables[1]:
            query = f"SELECT jobid FROM {self.tablename_users_jobs} WHERE userid=? AND status IS NOT NULL"

        try:
            with sqlite3.connect(DB_PATH, timeout=20.) as conn:
                cur = conn.cursor()

                cur.execute(query, (user_id,))
                
                return [row[0] for row in cur.fetchall()]
        except Exception as e:
            print(f"ERROR 1st query get_stored_jobs: {e}")
            return []
        
        return []

    def get_jobs_byID(self, job_ids):
        # created a string of ?, ?, ?... for how many job_ids it received
        placeholders = ", ".join(['?'] * len(job_ids))
        query = f"SELECT * FROM {self.tablename_jobs} WHERE id IN ({placeholders})"
        try:
            with sqlite3.connect(DB_PATH, timeout=20.0) as conn:
                cur = conn.cursor()

                cur.execute(query, job_ids)
                return cur.fetchall()
        except Exception as e:
            print(f"ERROR get_jobs_byID: {e}")
            return []
