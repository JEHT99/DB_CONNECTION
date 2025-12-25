import os
import psycopg2
from absDb import AbsDb
from dotenv import load_dotenv
#------------------------------------------------------------------
load_dotenv()
#------------------------------------------------------------------
class PostgreSQL(AbsDb):
    def _startConnection(self)-> (object|None):
        try:
            return psycopg2.connect(
                            database = os.getenv("DATABASE"), 
                            user = os.getenv("USER"), 
                            host= os.getenv("HOST"),
                            password = os.getenv("PASSWORD"),
                            port = os.getenv("PORT")
                            )
        except Exception as e:
            print(e)
            return None
#------------------------------------------------------------------