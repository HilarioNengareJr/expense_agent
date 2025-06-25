# ---------------------------------
# Register the Add expenses tool
# ---------------------------------
from langchain.agents import Tool
from database.db import DataBase

# Create instance of the DataBase class 
db = DataBase() 

def add_expense_tool(input_str):
    return db.add_expense(input_str)

tool_add_expense = Tool(
    name="add_expense",
    func=add_expense_tool,
    description="""Adds an expense to the database.
    Try: 'Add R120 groceries on June 24.'"""
)