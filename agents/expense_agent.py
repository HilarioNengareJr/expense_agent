from crewai import Agent, Task, Crew
from llm.local_llm import get_local_llm
from tools.expense_tools import add_expense, view_expenses, delete_expense, plot_expenses

class ExpenseAgent:
    """An agent that helps users manage their expenses by adding, viewing, deleting, and plotting spending trends."""
    
    def __init__(self):
        self.llm = get_local_llm()
        self.agent  = Agent(
            role="Expense Manager",
            goal="""Help the user to manage their expenses by adding, viewing, deleting, and plotting spending trends, and providing insights on their financial habits. " \
            "Understand that the user will use natural commands to interact with you, and you will use the tools provided to accomplish the tasks.""",
            backstory="You an expert in personal finance, accountinng, bookkeeping, and expense management.",
            llm=self.llm,
            tools=[ 
                add_expense, 
                view_expenses, 
                delete_expense, 
                plot_expenses.tool
            ],
            verbose=True
        )

    def run(self, user_input: str):
        task = Task(
            description=f"Handle this command: {user_input}",
            agent=self.agent
        )
        crew = Crew(agents=[self.agent], tasks=[task])
        return crew.kickoff()