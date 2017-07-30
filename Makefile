install-env:
	virtualenv --no-site-packages venv && source venv/bin/activate

test:
	python setup.py test

.PHONY: test
