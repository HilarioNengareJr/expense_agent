# ---------------------------------
# Register the Add Expense Tool
# ---------------------------------
from langchain.agents import Tool
from database.db import DataBase

# Create instance of the DataBase class 
db = DataBase() 

# Define the tool
add_expense = Tool(
    name="add_expense",
    func=db.add_expense,
    description="""Adds an expense to the database.
    Try: 'Add R120 groceries on June 24.'"""
)
