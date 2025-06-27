# ---------------------------------
# Register the Get Expenses Tool
# ---------------------------------
from langchain.agents import Tool
from database.db import DataBase

# Instantiate the supabase client
db = DataBase()

# Define the tool
get_expenses = Tool(
    name="get_expenses",
    func=db.get_expenses,
    description="""Retrieves all expenses from the database.
    Returns a list of expenses."""
)
