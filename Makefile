
install:
	@pip install \
	--force-reinstall \
	.[dev]

test:
	@python setup.py test
