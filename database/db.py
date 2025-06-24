import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables from .env file
class Config:
    def __init__(self):
        self.SUPABASE_URL = os.getenv("SUPABASE_URL")
        self.SUPABASE_KEY = os.getenv("SUPABASE_KEY")
        supabase = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    def add_expense(self, text: str):
        """
        Parses a natural command lie:
        'Add R120 groceries on June 24.' 
        and adds the expense to the supabase database.
        """

        match =  re.search(r"R?(\\d+\\.?\\d*)\\s+(\\w+)(?:\\s+on\\s+(.+))?", text.lower())
        
