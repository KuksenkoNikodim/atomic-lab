import pytest
import random
from app import is_valid_email_address, get_user_status, process_user_data

# Фиксируем seed для воспроизводимости
random.seed(42)

class TestEmailValidation:
    """Given-When-Then тесты для валидации email"""
    
    def test_valid_email(self):
        # GIVEN корректный email
        email = "user@example.com"
        
        # WHEN проверяем валидацию
        result = is_valid_email_address(email)
        
        # THEN результат должен быть True
        assert result is True
    
    def test_invalid_email_without_at(self):
        # GIVEN email без символа @
        email = "userexample.com"
        
        # WHEN проверяем валидацию
        result = is_valid_email_address(email)
        
        # THEN результат должен быть False
        assert result is False

class TestUserStatus:
    """Given-When-Then тесты для статуса пользователя"""
    
    def test_active_status(self):
        # GIVEN код статуса 1
        status_code = 1
        
        # WHEN получаем описание статуса
        status = get_user_status(status_code)
        
        # THEN должен вернуться "Active"
        assert status == "Active"
    
    def test_unknown_status(self):
        # GIVEN неизвестный код статуса
        status_code = 99
        
        # WHEN получаем описание статуса
        status = get_user_status(status_code)
        
        # THEN должен вернуться "Unknown"
        assert status == "Unknown"

class TestProcessUserData:
    """Given-When-Then тесты для обработки данных пользователя"""
    
    def test_valid_user_processing(self, mocker):
        # GIVEN валидные данные пользователя
        user_data = {
            "name": "John",
            "email": "john@example.com",
            "age": 25
        }
        
        # Mock API вызова
        mocker.patch('requests.get')
        
        # WHEN обрабатываем данные
        result = process_user_data(user_data)
        
        # THEN результат не должен быть None
        assert result is not None
        assert result['account_status'] == 'active'
    
    def test_underage_user(self):
        # GIVEN несовершеннолетний пользователь
        user_data = {
            "name": "Jane",
            "email": "jane@example.com",
            "age": 16
        }
        
        # WHEN обрабатываем данные
        result = process_user_data(user_data)
        
        # THEN результат должен быть None
        assert result is None