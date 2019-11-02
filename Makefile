
install:
	@pip install \
	--force-reinstall \
	.

test:
	@pytest

dist:
	@python setup.py sdist bdist_wheel

clean:
	@rm -rf \
	dist/ \
	build/ \
	.tox/ \
	.pytest_cache
