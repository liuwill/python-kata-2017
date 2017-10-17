install-env:
	virtualenv --no-site-packages venv && source venv/bin/activate

run-dev:
	source venv/bin/activate

test:
	python setup.py test

test-cov:
	py.test -xv --cov=kata

test-coverage:
	coverage run -m pytest

.PHONY: test
