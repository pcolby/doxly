# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

default: check

.PHONY: check coverage coverage-html lint pycodestyle pylint test

check: lint test

coverage:
	coverage run --module --source src unittest discover
	coverage report

coverage-html: coverage
	coverage html

lint: pycodestyle pylint

pycodestyle:
	pycodestyle src

pylint:
	pylint src

test:
	python -m unittest discover -v
