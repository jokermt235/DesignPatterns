from InsertCommand import InsertCommand
from SelectCommand import SelectCommand
from UpdateCommand import UpdateCommand
from DeleteCommand import DeleteCommand
class Developer:
    insert = None
    select = None
    update = None
    delete = None
    def __init__(self, insert : InsertCommand, select : SelectCommand, update : InsertCommand, delete : SelectCommand):
        self.insert = insert
        self.select = select
        self.update = update
        self.delete = delete
    
    def insertRecord(self):
        self.insert.execute()

    def selectRecord(self):
        self.select.execute()
    
    def updateRecord(self):
        self.update.execute()

    def deleteRecord(self):
        self.delete.execute()