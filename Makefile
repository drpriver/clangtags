wheelhouse: ; mkdir $@
civenv:
	python3 -m venv civenv
	civenv/bin/pip install build twine
.PHONY: wheel
wheel: | civenv  wheelhouse
	rm -f dist/*.whl
	civenv/bin/python -m build --wheel
	cp dist/*.whl wheelhouse

.PHONY: pypi-upload
pypi-upload:
	civenv/bin/python3 -m twine upload wheelhouse/* --verbose
