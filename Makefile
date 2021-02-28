pre: requirements.txt
	pip install -r requirements.txt

test:
	PYTHONPATH=. python -m unittest discover -v test

main: bin/main.py
	PYTHONPATH=. python bin/main.py

.PHONY: pre test main
