.PHONY: default all
default: collect_from_paycheck
all: flow collect_from_raw flow3

.PHONY: flow collect_from_raw flow3 collect_from_paycheck
flow:
	python flow.py $(WHERE)

collect_from_raw:
	python collect_from_raw.py $(WHERE)

flow3:
	python flow3.py $(WHERE)

collect_from_paycheck:
	python collect_from_paycheck.py $(WHERE)

.PHONY: consultant
consultant:
	# Do not forget to set the environment variables before running!
	flask run
