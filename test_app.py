import pytest
from app import validate_email, get_user_status, process_user_data

class TestValidateEmail:
    def test_valid_email(self):
        assert validate_email("user@example.com") == True

    def test_invalid_email_no_at(self):
        assert validate_email("userexample.com") == False

    def test_empty_email(self):
        assert validate_email("") == False

class TestGetUserStatus:
    def test_active_user(self):
        status_map = {"user1": "active"}
        assert get_user_status("user1", status_map) == "active"

    def test_inactive_user(self):
        status_map = {"user1": "inactive"}
        assert get_user_status("user1", status_map) == "inactive"

    def test_user_without_status(self):
        status_map = {}
        assert get_user_status("user1", status_map) == "unknown"

class TestProcessUserData:
    def test_process_valid_user(self):
        user = {"name": "John", "email": "john@example.com", "status": "active"}
        assert process_user_data(user) == "Processing user: John (status: active)"

    def test_process_invalid_email(self):
        user = {"name": "John", "email": "invalid", "status": "active"}
        assert process_user_data(user) == "Invalid email"
