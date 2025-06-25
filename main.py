from crewai import Agent, Task, Crew
from llm.local_llm import get_local_llm
from tools import add_expense, get_expenses, delete_expense

    
# ------------------------------
# Instantiate the llm object   
# ------------------------------
llm = get_local_llm()

    
# ------------------------------
# Create the expense agent 
# ------------------------------
expense_agent = Agent(
    
)