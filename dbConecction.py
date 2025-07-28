import os
import time
import psycopg2
from functools import wraps
from dotenv import load_dotenv
#------------------------------------------------------------------
load_dotenv()
#------------------------------------------------------------------
def VerifyConnection(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        sql = "SELECT 1;"
        try:
            with (self.client).cursor() as cursor:
                cursor.execute(sql)
        except:
            if self.client:
                (self.client).close()
            self.client = self._reconect()
        return func(self, *args, **kwargs)
    return wrapper
#------------------------------------------------------------------
class PostgreSQL():
    def __init__(self):
        self.client = self.__startConnection()
    #--------------------------------------------------------------
    def __del__(self):
        if self.client:
            (self.client).close()
    #--------------------------------------------------------------
    def __startConnection(self)-> (object|None):
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
    #--------------------------------------------------------------
    def _reconect(self)-> (object|None):
        attemps = 3
        while attemps > 0:
            time.sleep(1)
            client = self.__startConnection()
            if client is not None:
                break
            attemps -= 1
        return client        
#------------------------------------------------------------------