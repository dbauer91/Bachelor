import sqlite3

class DatabaseService:
    def __init__(self):
        self.connection = sqlite3.connect('../Resources/Database/measurement.sqlite3')
        self.cursor = self.dbConnection.cursor()
        
    def execute(self, command: str):
        self.connection.execute(command)
        self.cursor.commit()
        
    def query(self, command: str) -> str:
        return self.connection.execute(command)
    
    def close(self):
        self.conneciton.close()