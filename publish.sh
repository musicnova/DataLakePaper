#!/bin/sh
python setup.py sdist upload -r pypitest
python setup.py sdist upload -r pypi
python setup.py sdist
twine upload dist/*
