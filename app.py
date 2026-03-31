import requests
import logging

# REFACTOR: переименование переменных для ясности
def is_valid_email_address(email_string):
    if "@" not in email_string:
        return False
    return True

# FIX: добавлена обработка ошибок
def authenticate_user(credentials):
    try:
        if not credentials or 'username' not in credentials:
            raise ValueError("Invalid credentials format")
        # Аутентификационная логика
        return True
    except Exception as e:
        logging.error(f"Authentication failed: {e}")
        return False

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

def process_user_data(user_info):
    # Бизнес-логика с обновленными именами переменных
    if not is_valid_email_address(user_info['email']):
        print("Invalid email")
        return None
    
    if user_info['age'] < 18:
        print("User is underage")
        return None
    
    user_info['account_status'] = 'active'
    print(f"Processing user: {user_info['name']}")
    
    # Добавлена обработка ошибок для API вызова
    try:
        response = requests.get('https://api.example.com/users', timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"API call failed: {e}")
        return None
    
    return user_info

if __name__ == "__main__":
    user_data = {"name": "John", "email": "john@example.com", "age": 25}
    result = process_user_data(user_data)
    print("Result:", result)
    
    # Тестирование новой функции
    status = get_user_status(1)
    print(f"User status: {status}")