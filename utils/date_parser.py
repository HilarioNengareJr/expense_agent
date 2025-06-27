from datetime import datetime

def parse_date(text: str):
    try:
        return datetime.strptime(text, "%B %d").date().replace(year=datetime.today().year)
    except:
        return datetime.today().date()
    