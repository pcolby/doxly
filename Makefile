default: check

.PHONY: check
check: doxysaurus
	pycodestyle $<
	pylint $<
