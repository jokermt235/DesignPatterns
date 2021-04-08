from Database import Database
from Developer import Developer
from InsertCommand import InsertCommand
from SelectCommand import SelectCommand
from UpdateCommand import UpdateCommand
from DeleteCommand import DeleteCommand

database = Database()

dev = Developer(
    InsertCommand(database),
    SelectCommand(database),
    UpdateCommand(database),
    DeleteCommand(database)
)

dev.insertRecord()
dev.selectRecord()
dev.updateRecord()
dev.deleteRecord()