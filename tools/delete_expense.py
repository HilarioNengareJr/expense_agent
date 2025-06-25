#----------------------------------
# Register the Delete Expense Tool             
#----------------------------------
from langchain.agents import Tool
from database.db import DataBase

# Initialize the supabase db client
db = DataBase()

def delete_expense_tool(expense_id):
    return db.delete_expense(expense_id)

tool_delete_expense = Tool(
    name="delete_expense",
    func=delete_expense_tool,
    description="""Deletes an expense from the database by its ID.
        Returns a success message if the deletion was successful."""
)