import sqlite3
import mysql.connector


class SQLite3DatabaseConnection:
    def __init__(self, host: str) -> None:
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type: type, exc_val: sqlite3.OperationalError, exc_tb) -> None:
        if exc_tb or exc_val or exc_type:
            print(f"Error : \n        exc_type = {exc_type}\n        exc_val  = {exc_val}\n        exc_tb   = {exc_tb}")
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()


class MySQLDatabaseContextManager:
    def __init__(self, host, username, password, database=None):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        self.connection = None

    def __enter__(self):
        vals = {'host': self.host, 'username': self.username, 'password': self.password}
        if self.database:
            vals.update({"database": self.database})
        self.connection = mysql.connector.connect(**vals)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not (exc_tb or exc_val or exc_type):
            try:
                self.connection.commit()
            except:
                pass
        try:
            self.connection.close()
        except:
            pass
