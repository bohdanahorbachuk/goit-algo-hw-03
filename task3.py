import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр і знаку '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number.strip())
    
    # Перевіряємо наявність міжнародного коду
    if not phone_number.startswith('+'):
        if phone_number.startswith('380'):  # Якщо номер починається з '380', додаємо '+'
            phone_number = '+' + phone_number
        elif phone_number.startswith('0'):  # Якщо номер починається з '0', додаємо '+38'
            phone_number = '+38' + phone_number
        elif phone_number.startswith(''):  # Якщо номер починається з цифри, додаємо '+38'
            phone_number = '+38' + phone_number
        
    return phone_number

# Вхідні дані
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Нормалізовані номери
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

