# ---------------------------------
# Register the Delete Expense Tool             
# ---------------------------------
from langchain.agents import Tool
from database.db import DataBase

# Initialize the supabase db client
db = DataBase()

# Define the tool
delete_expense = Tool(
    name="delete_expense",
    func=db.delete_expense,
    description="""Deletes an expense from the database by its ID.
    Returns a success message if the deletion was successful."""
)
