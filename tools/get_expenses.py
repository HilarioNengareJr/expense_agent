# ---------------------------------
# Register the Get expenses tool
# ---------------------------------
from langchain.agents import Tool
from database.db import DataBase

# Instantiate the supabase client
db = DataBase()

def get_expenses_tool():
    return db.get_expenses()

tool_get_expenses = Tool(
    name="get_expenses",
    func=get_expenses_tool,
    description="""etrieves all expenses from the database.
    Returns a list of expenses."""
)