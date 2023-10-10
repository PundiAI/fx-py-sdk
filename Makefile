.PHONY: init
init:
	python -m pip install -r requirements.txt

.PHONY: test
test:
	python -m pytest tests

.PHONY: lint
lint:
	python -m flake8 --exclude=x --ignore=E501 fxsdk
