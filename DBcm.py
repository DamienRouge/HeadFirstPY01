import mysql.connector

class UseDatabase():
    def __init__(self,config:dict)->None:
        self.configuration = config
    def __enter__(self)->'cursor':
        #this is what as "cursor" is, a actual cursor returned by the "With"statement 
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor
    def __exit__(self,exc_type,exc_value,exc_trace)->None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
