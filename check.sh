#!/usr/bin/bash

python -m pip install --upgrade pip

if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f dev-requirements.txt ]; then pip install -r dev-requirements.txt; fi
pip install --editable .

pycodestyle karnbot/ tests/
black -t py36 --check karnbot/ tests/
pytest
