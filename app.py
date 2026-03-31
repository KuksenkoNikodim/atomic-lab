import requests

def validate_email(email):
    if "@" not in email:
        return False
    return True

def process_user_data(user_data):
    # Бизнес-логика
    if not validate_email(user_data['email']):
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

# Вывод в консоль
if __name__ == "__main__":
    user = {"name": "John", "email": "john@example.com", "age": 25}
    result = process_user_data(user)
    print("Result:", result)