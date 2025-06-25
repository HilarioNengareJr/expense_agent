# ---------------------------------
# Define Database functionalities
# ---------------------------------
import os
import re
from supabase import create_client
from utils.date_parser import parse_date


class DataBase:
    """Configuration class for Supabase client.
    This class initializes the Supabase client using environment variables. 
    It provides a method to add expenses to the database, get all the expenes and remove an expense as well.
    """
    
    # ------------------------------
    # Initialize Supabase Client    
    # ------------------------------
    def __init__(self):
        self.SUPABASE_URL = os.getenv("SUPABASE_URL")
        self.SUPABASE_KEY = os.getenv("SUPABASE_KEY")
        self.supabase = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    # ------------------------------
    # Add Expense Method
    # ------------------------------
    def add_expense(self, text: str):
        """
        Parses a natural command line:
        'Add R120 groceries on June 24.' 
        and adds the expense to the supabase database.
        """

        match =  re.search(r"R?(\\d+\\.?\\d*)\\s+(\\w+)(?:\\s+on\\s+(.+))?", text.lower()) # look for currency, item, and date

        if not match:
            return "Could not parse the command. Please use the format: 'Add R120 groceries on June 24.'"

        amount = float(match.group(1))
        category = match.goup(2)
        date = match.group(3)
        parsed_date = parse_date(date) if date else date.today()

        result = self.supabase.table("expenses").insert({
            "amount": amount,
            "category": category,
            "date": parsed_date.isoformat()
        }).execute()

        if result.data: return f"Added R{amount} for {category} on {parsed_date}." # return success message after adding expense

    #-------------------------------
    # Get Expenses Method
    #-------------------------------
    def get_expenses(self):
        """
        Retrieves all expenses from the database.
        Returns a list of expenses.
        """

        result = self.supabase.table("expenses").select("*").order("date", desc=True).execute() 
        return result.data or []

    #-------------------------------
    # Delete Expense Method             
    #-------------------------------
    def delete_expense(self, expense_id: int):
        """
        Deletes an expense from the database by its ID.
        Returns a success message if the deletion was successful.
        """
        return self.supabase.table("expenses".delete().eq("id", expense_id).execute())