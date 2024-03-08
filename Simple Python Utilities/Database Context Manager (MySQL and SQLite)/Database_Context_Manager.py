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


class MySQLDatabaseConnection:
    def __init__(self, host, username, password):
        self.connection = None
        self.host = host
        self.username = username
        self.password = password

    def __enter__(self):
        self.connection = mysql.connector.connect(host=self.host, user=self.username, password=self.password)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_val or exc_type:
            print(f"Error : \n        exc_type = {exc_type}\n        exc_val  = {exc_val}\n        exc_tb   = {exc_tb}")
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
