from crewai import Agent, Task, Crew
from llm.local_llm import get_local_llm
from tools import tool_list

    
# ------------------------------
# Instantiate the llm object   
# ------------------------------
llm = get_local_llm()

    
# ------------------------------
# Create the expense agent 
# ------------------------------
expense_agent = Agent(
    role="Expense Manager",
    goal="Help the user manage personal expenses via natural language",
    backstory="A smart assistant trained to understand your expenses and manage them efficiently.",
    llm=llm,
    tools=tool_list
)

# ------------------------------
# Function to run the task 
# ------------------------------
def run_expense_command(user_input: str):
    task = Task(
        description=f"Handle this user command : '{user_input}'",
        agent=expense_agent
    )

    crew = Crew(
        agents=[expense_agent],
        tasks=[task]
    )

    return crew.kickoff()

# ------------------------------
# CLI loop
# ------------------------------
if __name__ == "__main__":
    print("Expense Manager is ready. Tpe your command or ('exit') ")

    while True:
        user_input = input(">> ").strip()
        if (user_input.lower in ["exit", "quit"]):
            break

        response = run_expense_command(user_input)
        print(f"\nResponse is \n{response}")