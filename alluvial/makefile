.PHONY: default all
default: collect_from_paycheck
all: flow collect_from_raw flow3

PY = python3
ifeq ($(OS), Windows_NT)
	PY = python
endif

.PHONY: flow collect_from_raw flow3 collect_from_paycheck
flow:
	$(PY) flow.py $(WHERE)

collect_from_raw:
	$(PY) collect_from_raw.py $(WHERE)

flow3:
	$(PY) flow3.py $(WHERE)

collect_from_paycheck:
	$(PY) collect_from_paycheck.py $(WHERE)

.PHONY: consultant
consultant:
	FLASK_APP=consultant.py flask run
