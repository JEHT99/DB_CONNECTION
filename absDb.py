import time
from functools import wraps
from abc import ABC, abstractmethod
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
class AbsDb():
    def __init__(self):
        self.client = self._startConnection()
    #--------------------------------------------------------------
    def __del__(self):
        if self.client:
            (self.client).close()
    #--------------------------------------------------------------
    @abstractmethod
    def _startConnection(self)-> (object|None):
        pass
    #--------------------------------------------------------------
    def _reconect(self)-> (object|None):
        attemps = 3
        while attemps > 0:
            time.sleep(1)
            client = self._startConnection()
            if client is not None:
                break
            attemps -= 1
        return client
    #--------------------------------------------------------------
    @VerifyConnection
    def getdata(self, sql:str, values:tuple=())-> list:
        if self.client is None:
            return []
        
        cursor = None
        try:
            cursor = (self.client).cursor()
            cursor.execute(sql, values)
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return []
        finally:
            if cursor:
                cursor.close()
    #--------------------------------------------------------------
    @VerifyConnection
    def setData(self, sql:str, values:tuple=())-> bool:
        if self.client is None:
            return False
                
        cursor = None
        try:
            cursor = (self.client).cursor()
            cursor.execute(sql, values)
            (self.client).commit()
            return True
        except Exception as e:
            print(e)
            (self.client).rollback()
            return False
        finally:
            if cursor:
                cursor.close()
    #--------------------------------------------------------------
    @VerifyConnection
    def setDataReturning(self, sql:str, values:tuple=())-> list:
        if self.client is None:
            return []
        
        cursor = None
        try:
            cursor = (self.client).cursor()
            cursor.execute(sql, values)
            data = cursor.fetchall()
            (self.client).commit()
            return data
        except Exception as e:
            print(e)
            (self.client).rollback()
            return []
        finally:
            if cursor:
                cursor.close()
    #--------------------------------------------------------------
#------------------------------------------------------------------