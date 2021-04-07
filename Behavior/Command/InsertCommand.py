from Command import Command
from Database import Database
class InsertCommand(Command):
    database = None
    def __init__(self, database : Database):
        self.database = database
    def execute(self):
        self.database.insert()