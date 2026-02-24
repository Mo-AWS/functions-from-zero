install:
	pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py
