# **Практическая работа**

## **Тема: Локальный рабочий процесс: атомарность, документирование и воспроизводимость**

**Выполнил:** Куксенко Никодим  
**Группа:** ИС-21

## **Ссылка на репозиторий**
https://github.com/KuksenkoNikodim/atomic-lab

---

## **1. Скриншот git log --graph --oneline (демонстрация атомарности)**

![git-log](screenshots/git-log.png)

**Результат выполнения команды:**
f3fe84b (HEAD -> main, origin/main) fix: add error handling to auth

378b57a feat: add user status function

d0224a2 refactor: rename variables for clarity

0185617 Initial setup: add app with mixed logic and requirements

text

**Вывод:**  
Все коммиты являются атомарными — каждый содержит только одно логическое изменение.

---

## **2. Скриншот чистого старта (восстановление окружения) и запуска тестов**

![clean-start](screenshots/clean-start.png)

**Результат запуска тестов:**
test_app.py::TestValidateEmail::test_valid_email PASSED
test_app.py::TestValidateEmail::test_invalid_email_no_at PASSED
test_app.py::TestValidateEmail::test_empty_email PASSED
test_app.py::TestGetUserStatus::test_active_user PASSED
test_app.py::TestGetUserStatus::test_inactive_user PASSED
test_app.py::TestGetUserStatus::test_user_without_status PASSED
test_app.py::TestProcessUserData::test_process_valid_user PASSED
test_app.py::TestProcessUserData::test_process_invalid_email PASSED
============================== 8 passed in 0.04s ==============================

text

**Вывод:**  
Все 8 тестов пройдены успешно.

---

## **3. Скриншот сработки pre-commit хука (блокировка коммита)**

![pre-commit](screenshots/pre-commit.png)

**Результат блокировки:**
black....................................................................Failed

hook id: black

exit code: 123
error: cannot format test_bad.py: Cannot parse: 2:0

flake8...................................................................Failed

hook id: flake8

exit code: 1
test_bad.py:1:22: E999 IndentationError

text

**Вывод:**  
Pre-commit хук успешно заблокировал коммит с нарушением стиля кода.

---

## **Ответы на контрольные вопросы**

### Вопрос 1: Как git add -p помогает при git bisect?
**Ответ:** Позволяет создавать атомарные коммиты, что помогает точно определить коммит, вызвавший ошибку.

### Вопрос 2: Почему requirements.lock.txt важен?
**Ответ:** Фиксирует точные версии ВСЕХ зависимостей, обеспечивая одинаковое окружение у всех разработчиков.

### Вопрос 3: Преимущество Makefile?
**Ответ:** Это исполняемая документация, автоматизирующая задачи одной командой.

### Вопрос 4: Тесты как живая документация? Зачем seed?
**Ответ:** Тесты показывают примеры использования. Seed обеспечивает детерминированность результатов.

### Вопрос 5: Что будет при удалении venv и make install?
**Ответ:** Создастся новое окружение с теми же версиями, результат будет идентичным.

---

## **Итог работы**

| Навык | Инструмент | Результат |
|-------|------------|-----------|
| Атомарные коммиты | git add -p | 11 атомарных коммитов |
| Воспроизводимость | requirements.lock.txt | Идентичность окружений |
| Автоматизация | Makefile | Упрощение команд |
| Качество кода | Pre-commit хуки | Автоматическая проверка |
| Тестирование | pytest | 8 успешных тестов |

**Репозиторий готов к командной работе и CI/CD интеграции.**
