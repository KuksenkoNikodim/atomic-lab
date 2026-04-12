install:
	pip install -r requirements.txt
	pip freeze > requirements.lock.txt

test:
	pytest test_app.py -v

run:
	python app.py

clean:
	rm -rf venv __pycache__ .pytest_cache

.PHONY: install test run clean
