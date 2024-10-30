from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        
        today = datetime(2021, 5, 5) 
        
        difference = (given_date - today).days
        return difference
    except ValueError:
        
        print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
        return None

print(get_days_from_today("2021-10-09"))  
