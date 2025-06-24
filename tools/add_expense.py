from langchain.agents import Tool
from database.db import add_expense_to_db

def tool_function(input_str):
    return add_expense_to_db(input_str)

tool = Tool(
    name="add_expense",
    func=tool_function,
    description="""Adds an expense to the database. Try: 'Add R120 groceries on June 24.'"""
)