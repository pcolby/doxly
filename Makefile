# SPDX-FileCopyrightText: 2024 Paul Colby <git@colby.id.au>
# SPDX-License-Identifier: GPL-3.0-or-later

doxml-dir = ${HOME}/tmp/build/dokit-gcc-6.6.3-debug/doc/xml
template = docusaurus
output-dir = ${HOME}/tmp/doxly/output

.PHONY: build check coverage coverage-html lint pycodestyle pylint run-module run-pipx test

default: build

build:
	python -m build

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

run-module:
	cd src && python -m doxly -i '${doxml-dir}' -t '${template}' -o '${output-dir}'

run-pipx:
	pipx run --no-cache --spec . doxly -i '${doxml-dir}' -t '${template}' -o '${output-dir}'

test:
	python -m unittest discover -v
