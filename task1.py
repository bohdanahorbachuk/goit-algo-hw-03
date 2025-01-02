from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка у формат дати
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Отримання поточної дати без часу
        today = datetime.today().date()
        
        # Обчислення різниці в днях
        difference = (given_date - today).days
        return difference
    except ValueError:
        print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
        return None

# Приклад використання
print(get_days_from_today("2025-01-04"))  
