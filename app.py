import requests

def is_valid_email_address(email_string):
    if "@" not in email_string:
        return False
    return True

# FEAT: новая функция статуса пользователя
def get_user_status(user_status_code):
    """
    Get user status description based on status code
    """
    status_map = {
        1: "Active",
        2: "Inactive",
        3: "Suspended",
        4: "Pending"
    }
    return status_map.get(user_status_code, "Unknown")

def process_user_data(user_data):
    # Бизнес-логика
    if not is_valid_email_address(user_data['email']):
        print("Invalid email")
        return None
    
    # Валидация
    if user_data['age'] < 18:
        print("User is underage")
        return None
    
    # Обработка данных
    user_data['status'] = 'active'
    print(f"Processing user: {user_data['name']}")
    
    # Внешний API вызов
    response = requests.get('https://api.example.com/users')
    return user_data

if __name__ == "__main__":
    user = {"name": "John", "email": "john@example.com", "age": 25}
    result = process_user_data(user)
    print("Result:", result)
    
    # Тестирование новой функции
    status = get_user_status(1)
    print(f"User status: {status}")