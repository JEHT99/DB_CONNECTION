import os
import sqlite3
from absDb import AbsDb
from dotenv import load_dotenv
#------------------------------------------------------------------
load_dotenv()
#------------------------------------------------------------------
class SQLite(AbsDb):
    def _startConnection(self)-> (object|None):
        db = os.getenv("DATABASE")
        if db is None:
            return None
        
        if not db.endswith(".db"): 
            return None
        
        if db not in os.listdir():
            return None
        
        try:
            return sqlite3.connect(db)
        except Exception as e:
            print(e)
            return None
#------------------------------------------------------------------