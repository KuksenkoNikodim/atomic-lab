import random

def validate_email(email):
    if not email or "@" not in email:
        return False
    return True

def get_user_status(user_id, status_map):
    return status_map.get(user_id, "unknown")

def process_user_data(user):
    if not validate_email(user.get("email", "")):
        return "Invalid email"
    return f"Processing user: {user.get('name', 'Unknown')} (status: {user.get('status', 'inactive')})"

if __name__ == "__main__":
    random.seed(42)
    user = {"name": "John", "email": "john@example.com", "status": "active"}
    print(process_user_data(user))
